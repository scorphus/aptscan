#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of aptscan
# https://github.com/scorphus/aptscan

# Licensed under the BSD-3-Clause license:
# https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2024, Pablo S. Blum de Aguiar <scorphus@gmail.com>

import pytest

from aptscan import scanner


def test_scanner_can_parse_one_room():
    floor_plan = """+--------+
|(room a)|
|       C|
|       C|
|       C|
+--------+
"""
    s1 = scanner.Scanner(floor_plan)
    assert s1.get_floor_map_repr() == floor_plan.replace("(room a)", "        ")
    assert s1.rooms == {(1, 1): "room a"}


def test_scanner_can_parse_multiple_rooms():
    floor_plan = """+--------+--------+
|(room a)|(room b)|
|       C|       C|
|       C|       C|
|       C|       C|
+--------+--------+
"""
    s1 = scanner.Scanner(floor_plan)
    expected_repr = floor_plan.replace("(room a)", "        ").replace("(room b)", "        ")
    assert s1.get_floor_map_repr() == expected_repr
    assert s1.rooms == {(1, 1): "room a", (1, 10): "room b"}


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
