#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of aptscan
# https://github.com/scorphus/aptscan

# Licensed under the BSD-3-Clause license:
# https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2024, Pablo S. Blum de Aguiar <scorphus@gmail.com>

"""provides a scanner that reads a floor plan and counts the number of chairs in
each room. Example of a room with 3 chairs:

    +----------+
    |          |
    | (room a) |
    |        C |
    |        C |
    |        C |
    |          |
    +----------+

"""

import itertools
from typing import Dict, Iterable, Tuple


EMPTY = " "
CHAIRS = ["W", "P", "S", "C"]
WALLS = ["+", "-", "|", "/", "\\"]
ROOM_NAME_OPEN = "("
ROOM_NAME_CLOSE = ")"

Position = Tuple[int, int]


class Room:
    """Room represents a room in a floor plan"""

    name: str
    chairs: Dict[str, int]

    def __init__(self, name: str, chairs: Dict[str, int]) -> None:
        self.name = name
        self.chairs = chairs


class Scanner:
    """Scanner reads a floor plan and counts the number of chairs in each room"""

    floor_map: Dict[Position, str]
    rooms: Dict[Position, Room]

    def __init__(self, floor_plan: str) -> None:
        self.floor_map = {}
        self.rooms = {}
        self._parse(floor_plan)
        try:
            self._count_chairs()
        except KeyError as err:
            raise ValueError("invalid floor plan: floor plan is malformed") from err

    def _parse(self, floor_plan: str) -> None:
        """Parse the floor plan and populate the floor map and rooms"""
        for row, line in enumerate(floor_plan.splitlines()):
            col = 0
            line_iter = iter(line)
            while char := next(line_iter, None):
                match char:
                    case c if c == ROOM_NAME_OPEN:
                        room_name = "".join(
                            itertools.takewhile(lambda c: c != ROOM_NAME_CLOSE, line_iter)
                        )
                        for i in range(col, col + len(room_name) + 2):
                            self.floor_map[(row, i)] = EMPTY
                        self.rooms[(row, col)] = Room(room_name, {chair: 0 for chair in CHAIRS})
                        col += len(room_name) + 2
                    case c if c == ROOM_NAME_CLOSE:
                        raise ValueError("invalid floor plan: unexpected closing parenthesis")
                    case _:
                        self.floor_map[(row, col)] = char
                        col += 1

    def _count_chairs(self) -> None:
        """Count the number of chairs in each room storing the result in the room object"""
        for room_pos, room in self.rooms.items():
            next_squares = set([room_pos])
            seen = set([room_pos])
            while next_squares:
                square = next_squares.pop()
                if self.floor_map[square] in CHAIRS:
                    room.chairs[self.floor_map[square]] += 1
                elif self.floor_map[square] is not EMPTY:
                    raise ValueError(f"invalid floor plan: unexpected character at {square}")
                for neighbor in self._get_neighbors(square):
                    if neighbor not in seen:
                        next_squares.add(neighbor)
                        seen.add(neighbor)

    def _get_neighbors(self, square: Position) -> Iterable[Position]:
        """Return the neighbors of a square"""
        row, col = square
        for neighbor in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
            if self.floor_map.get(neighbor, None) not in WALLS:
                yield neighbor

    def get_floor_map_repr(self) -> str:
        """Return a string representation of the floor map"""

        def generate_squares() -> Iterable[str]:
            row = col = 0
            while True:
                square = self.floor_map.get((row, col), None)
                if not square:
                    row += 1
                    col = 0
                    yield "\n"
                square = self.floor_map.get((row, col), None)
                if not square:
                    break
                yield square
                col += 1

        return "".join(generate_squares())
