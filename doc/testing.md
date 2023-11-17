# Automated testing

## Introduction

The bash-completion package contains an automated test suite. Running the
tests should help verifying that bash-completion works as expected. The tests
are also very helpful in uncovering software regressions at an early stage.

The test suite is written in Python, using [pytest](https://pytest.org/)
and [pexpect](https://pexpect.readthedocs.io/).

## Coding style

For the Python part, all of it is checked and formatted using
[Ruff](https://docs.astral.sh/ruff/).

## Installing dependencies

Installing dependencies should be easy using your local package manager or
`pip`. Python 3.6 or newer is required, and the rest of the Python package
dependencies are specified in the `test/requirements.txt` file. If using `pip`,
this file can be fed directly to it, e.g. like:

```shell
python3 -m pip install -r test/requirements.txt
```

### Debian/Ubuntu

On Debian/Ubuntu you can use `apt-get`:

```shell
sudo apt-get install python3-pytest python3-pexpect
```

This should also install the necessary dependencies. Only Debian testing
(buster) and Ubuntu 18.10 (cosmic) and later have an appropriate version
of pytest in the repositories.

### Fedora/RHEL/CentOS

On Fedora and RHEL/CentOS (with EPEL) you can try `yum` or `dnf`:

```shell
sudo yum install python3-pytest python3-pexpect
```

This should also install the necessary dependencies. At time of writing, only
Fedora 29 comes with recent enough pytest.

## Structure

Tests are in the `t/` subdirectory, with `t/test_*.py` being completion
tests, and `t/unit/test_unit_*.py` unit tests.

## Running the tests

Tests are run by calling `pytest` on the desired test directories or
individual files, for example in the project root directory:

```shell
pytest test/t
```

See `test/docker/entrypoint.sh` for how and what we run and test in CI.

### Specifying bash binary

The test suite standard uses `bash` as found in `$PATH`. Export the
`bashcomp_bash` environment variable with a path to another bash executable if
you want to test against something else.

## Maintenance

### Adding a completion test

You can run `cd test && ./generate cmd` to add a test for the `cmd`
command. Additional arguments will be passed to the first generated test case.
This will add the `test/t/test_cmd.py` file with a very basic test, and add it
to `test/t/Makefile.am`. Add additional tests to the generated file.
