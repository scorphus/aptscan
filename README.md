# AptScan [![Build Status][build-badge]][action-link] [![Coverage Status][codecov-badge]][codecov-link] [![Maintainability][codeclimate-badge]][codeclimate-link] [![Code Quality][codacy-badge]][codacy-link]

## Apartment Floor Plan Scanner

AptScan swiftly scans floor plans, automating chair type counting for each room
in the floor plan. It provides the user with the number of chairs in each room
and the total number of chairs in the floor plan.

## Installation

To install, follow these steps:

1.  Create a Python virtual environment using your preferred choice ([pyenv][]
    is recommended)
2.  With the recently created virtual environment activated, install the package
    with the following command:

    ```shell
    make setup
    ```

> _Note: aptscan requires Python 3.10 or newer._

## Usage

To display the help message with the available commands and options, run:

```shell
aptscan --help
```

To scan a floor plan, use the `aptscan` console utility. Ex.:

```shell
aptscan rooms.txt
```

## Running tests

1.  Run tests with:
    ```shell
    make test
    ```
2.  And check code coverage with:
    ```shell
    make coverage
    open htmlcov/index.html
    ```

## Extra

1.  To see all available make targets:
    ```shell
    make list
    ```

## License

Code in this repository is distributed under the terms of the BSD 3-Clause
License (BSD-3-Clause).

See [LICENSE][] for details.

[build-badge]: https://github.com/scorphus/aptscan/workflows/Python/badge.svg
[action-link]: https://github.com/scorphus/aptscan/actions?query=workflow%3APython
[codecov-badge]: https://codecov.io/gh/scorphus/aptscan/branch/main/graph/badge.svg
[codecov-link]: https://codecov.io/gh/scorphus/aptscan
[codeclimate-badge]: https://api.codeclimate.com/v1/badges/0be26e2fab6a6964945f/maintainability
[codeclimate-link]: https://codeclimate.com/github/scorphus/aptscan/maintainability
[codacy-badge]: https://app.codacy.com/project/badge/Grade/7fb3fdf240f344d4b90c3c2ea87877bf
[codacy-link]: https://app.codacy.com/gh/scorphus/aptscan/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade
[pyenv]: https://github.com/pyenv/pyenv
[LICENSE]: LICENSE
