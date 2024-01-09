#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of aptscan
# https://github.com/scorphus/aptscan

# Licensed under the BSD-3-Clause license:
# https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2024, Pablo S. Blum de Aguiar <scorphus@gmail.com>

from aptscan import main


def test_get_floor_summary():
    floor_plan = r"""+---------+
|(library)|
|       W |
|     P P |
|   S S S |
| C C C C |
+---------+------------------+       +---+
|(bedroom)|                C |       | W |
|       C |   +----------+   |       |   |
|       C |   |          |   |       |   |
|       C +   +------+   |   |       |   |
|        C \(tunnel)/    |   |       |   |
|         C \      /     |   +-------+   |
|          C \    /      | S           P |
+-------------+--+       +---------------+
"""
    expected_summary = """total:
W: 2, P: 3, S: 4, C: 11
bedroom:
W: 0, P: 0, S: 0, C: 6
library:
W: 1, P: 2, S: 3, C: 4
tunnel:
W: 1, P: 1, S: 1, C: 1"""
    assert main.get_floor_summary(floor_plan) == expected_summary
