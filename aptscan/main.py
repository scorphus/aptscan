#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of aptscan
# https://github.com/scorphus/aptscan

# Licensed under the BSD-3-Clause license:
# https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2024, Pablo S. Blum de Aguiar <scorphus@gmail.com>

"""main contains the `aptscan` entry point along with main action"""

import argparse
import sys
from typing import Tuple

from aptscan import __doc__, __version__, scanner


def aptscan() -> None:  # pragma: no cover
    """Entry point for command line tool ``aptscan``.

    :Usage:

    .. code-block:: text

        $ aptscan --help  # to display help
        $ aptscan rooms.txt  # to scan rooms.txt

    """
    parser, parsed_args = parse_args()
    if parsed_args.version:
        print(f"aptscan {__version__}")
    elif parsed_args.plan_file:
        try:
            floor_plan = parsed_args.plan_file.read()
            print(get_floor_summary(floor_plan))
        except Exception as exc:  # pylint: disable=broad-except
            parser.print_usage()
            sys.stderr.write(f"aptscan: error: {exc}\n")
            sys.exit(1)
    else:
        parser.print_usage()


def get_floor_summary(floor_plan: str) -> str:
    """Return a summary of the floor plan"""
    floor_scanner = scanner.Scanner(floor_plan)
    summary_lines = ["total:", ""]
    total_chairs = {c: 0 for c in scanner.CHAIRS}
    for room in sorted(floor_scanner.rooms.values(), key=lambda r: r.name):
        summary_lines.append(f"{room.name}:")
        summary_lines.append(
            ", ".join(f"{chair}: {count}" for chair, count in room.chairs.items())
        )
        for chair_type, count in room.chairs.items():
            total_chairs[chair_type] += count
    summary_lines[1] = ", ".join(f"{chair}: {count}" for chair, count in total_chairs.items())
    return "\n".join(summary_lines)


def parse_args() -> Tuple[argparse.ArgumentParser, argparse.Namespace]:  # pragma: no cover
    """Parse arguments passed to the program"""
    parser = argparse.ArgumentParser(
        prog="aptscan",
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("-V", "--version", action="store_true", help="display program version")
    parser.add_argument(
        "plan_file",
        nargs="?",
        help="path to the file containing the floor plan",
        type=argparse.FileType("r"),
    )
    return parser, parser.parse_args()
