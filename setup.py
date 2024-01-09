#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of aptscan
# https://github.com/scorphus/aptscan

# Licensed under the BSD-3-Clause license:
# https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2024, Pablo S. Blum de Aguiar <scorphus@gmail.com>

import os

from setuptools import find_packages, setup

from aptscan import __version__


def read(*rnames):
    with open(os.path.join(os.path.dirname(__file__), *rnames), encoding="utf8") as f:
        return f.read()


extras_require = {
    "tests": [
        "autopep8",
        "black",
        "coverage",
        "flake8",
        "ipdb",
        "isort",
        "mypy",
        "pylint",
        "pytest",
        "pytest-asyncio",
        "pytest-cov",
        "pytest-mock",
    ],
}

setup(
    name="aptscan",
    version=__version__,
    url="https://github.com/scorphus/aptscan",
    license="BSD-3-Clause",
    description="Apartment Floor Plan Scanner",
    keywords="apartment floor plan scanner rooms chairs",
    long_description=read("README.md"),
    classifiers=[
        "License :: OSI Approved :: 3-Clause BSD License License",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    author="Pablo S. Blum de Aguiar",
    author_email="scorphus@gmail.com",
    packages=find_packages(),
    install_requires=[],
    extras_require=extras_require,
    entry_points={"console_scripts": ["aptscan = aptscan.main:aptscan"]},
    include_package_data=True,
    zip_safe=False,
)
