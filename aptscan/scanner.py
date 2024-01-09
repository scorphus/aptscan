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


ROOM_NAME_OPEN = "("
ROOM_NAME_CLOSE = ")"

Position = Tuple[int, int]


class Scanner:
    """Scanner reads a floor plan and counts the number of chairs in each room"""

    floor_map: Dict[Position, str]
    rooms: Dict[Position, str]

    def __init__(self, floor_plan: str) -> None:
        self.floor_map = {}
        self.rooms = {}
        self._parse(floor_plan)

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
                            self.floor_map[(row, i)] = " "
                        self.rooms[(row, col)] = room_name
                        col += len(room_name) + 2
                    case c if c == ROOM_NAME_CLOSE:
                        raise ValueError("invalid floor plan: unexpected closing parenthesis")
                    case _:
                        self.floor_map[(row, col)] = char
                        col += 1

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
