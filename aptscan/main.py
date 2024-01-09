#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of aptscan
# https://github.com/scorphus/aptscan

# Licensed under the BSD-3-Clause license:
# https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2024, Pablo S. Blum de Aguiar <scorphus@gmail.com>

"""main contains the `aptscan` entry point along with main action"""

import argparse
from typing import Tuple

from aptscan import __doc__, __version__


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
    else:
        parser.print_usage()


def parse_args() -> Tuple[argparse.ArgumentParser, argparse.Namespace]:  # pragma: no cover
    """Parse arguments passed to the program"""
    parser = argparse.ArgumentParser(
        prog="aptscan",
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("-V", "--version", action="store_true", help="display program version")
    return parser, parser.parse_args()
