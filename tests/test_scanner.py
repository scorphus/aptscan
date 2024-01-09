#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of aptscan
# https://github.com/scorphus/aptscan

# Licensed under the BSD-3-Clause license:
# https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2024, Pablo S. Blum de Aguiar <scorphus@gmail.com>

import pytest

from aptscan import scanner


@pytest.fixture(name="floor_plan")
def floor_plan_fixture():
    return """+--------+
|(room a)|
|       C|
|       C|
|       C|
+--------+
"""


@pytest.fixture(name="floor_plan_multi")
def floor_plan_multi_fixture():
    return """+--------+--------+
|(room a)|(room b)|
|       C|       C|
|       C|       C|
|       C|       C|
+--------+--------+
"""


def test_scanner_can_parse_one_room(floor_plan):
    s1 = scanner.Scanner(floor_plan)
    assert s1.get_floor_map_repr() == floor_plan.replace("(room a)", "        ")
    assert len(s1.rooms) == 1
    assert (1, 1) in s1.rooms
    assert s1.rooms[(1, 1)].name == "room a"


def test_scanner_can_parse_multiple_rooms(floor_plan_multi):
    s1 = scanner.Scanner(floor_plan_multi)
    expected_repr = floor_plan_multi.replace("(room a)", "        ").replace(
        "(room b)", "        "
    )
    assert s1.get_floor_map_repr() == expected_repr
    assert len(s1.rooms) == 2
    assert (1, 1) in s1.rooms
    assert s1.rooms[(1, 1)].name == "room a"
    assert (1, 10) in s1.rooms
    assert s1.rooms[(1, 10)].name == "room b"


def test_scanner_fails_to_parse_a_floor_plan_with_unexpected_closing_parenthesis():
    floor_plan = """+--------+
|)room a)|
|       C|
|       C|
|       C|
+--------+
"""
    with pytest.raises(ValueError) as excinfo:
        scanner.Scanner(floor_plan)
    assert str(excinfo.value) == "invalid floor plan: unexpected closing parenthesis"


def test_scanner_fails_to_parse_a_floor_plan_with_a_room_with_an_unclosed_name():
    floor_plan = """+--------+
|(room a |
|       C|
|       C|
|       C|
+--------+
"""
    with pytest.raises(ValueError) as excinfo:
        scanner.Scanner(floor_plan)
    assert str(excinfo.value) == "invalid floor plan: floor plan is malformed"


def test_scanner_fails_to_parse_a_floor_plan_with_a_room_with_invalid_object():
    floor_plan = """+--------+
|(room a)|
|       C|
|  X    C|
|       C|
+--------+
"""
    with pytest.raises(ValueError) as excinfo:
        scanner.Scanner(floor_plan)
    assert str(excinfo.value) == "invalid floor plan: unexpected character at (3, 3)"


@pytest.mark.parametrize(
    "floor_plan",
    [
        """+--------+
|(room a)|
|       C|
        C|
|       C|
+--------+
""",
        """+---- ---+
|(room a)|
|       C|
|       C|
|       C|
+--------+
""",
        """+--------+
|(room a)|
|       C|
|       C|
|       C|
+- ------+
""",
    ],
)
def test_scanner_fails_to_parse_malformed_floor_plans(floor_plan):
    with pytest.raises(ValueError) as excinfo:
        scanner.Scanner(floor_plan)
    assert str(excinfo.value) == "invalid floor plan: floor plan is malformed"


def test_scanner_can_count_chairs_in_one_room(floor_plan):
    s1 = scanner.Scanner(floor_plan)
    assert s1.rooms[(1, 1)].chairs == {"W": 0, "P": 0, "S": 0, "C": 3}


def test_scanner_can_count_chairs_in_multiple_rooms(floor_plan_multi):
    s1 = scanner.Scanner(floor_plan_multi)
    assert s1.rooms[(1, 1)].chairs == {"W": 0, "P": 0, "S": 0, "C": 3}
    assert s1.rooms[(1, 10)].chairs == {"W": 0, "P": 0, "S": 0, "C": 3}


def test_scanner_can_count_chairs_in_a_room_with_multiple_chair_types():
    floor_plan = """+--------+
|(room a)|
|       W|
|     P P|
|   S S S|
| C C C C|
+--------+
"""
    s1 = scanner.Scanner(floor_plan)
    assert s1.rooms[(1, 1)].chairs == {"W": 1, "P": 2, "S": 3, "C": 4}


def test_scanner_can_count_chairs_in_rooms_with_diagonal_walls():
    floor_plan = r"""+--------+------------------+      +---+
|(room a)|                C |      | W |
|       C|   +----------+   |      |   |
|       C|   |          |   |      |   |
|       C+   +------+   |   |      |   |
|        C\(room b)/    |   |      |   |
|         C\      /     |   +------+   |
|          C\    /      | S          P |
+------------+--+       +--------------+
"""
    s1 = scanner.Scanner(floor_plan)
    assert s1.rooms[(1, 1)].chairs == {"W": 0, "P": 0, "S": 0, "C": 6}
    assert s1.rooms[(5, 11)].chairs == {"W": 1, "P": 1, "S": 1, "C": 1}
