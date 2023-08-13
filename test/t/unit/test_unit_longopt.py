# Based on work by Stephen Gildea, October 2010.

import pytest

from conftest import assert_bash_exec


@pytest.mark.bashcomp(cmd=None, ignore_env=r"^\+COMPREPLY=")
class TestUnitLongopt:
    @pytest.fixture(scope="class")
    def functions(self, request, bash):
        assert_bash_exec(bash, "_grephelp() { cat _longopt/grep--help.txt; }")
        assert_bash_exec(bash, "complete -F _comp_complete_longopt _grephelp")
        assert_bash_exec(bash, "_various() { cat _longopt/various.txt; }")
        assert_bash_exec(bash, "complete -F _comp_complete_longopt _various")

    @pytest.mark.complete("_grephelp --")
    def test_1(self, functions, completion):
        """First long option should be included"""
        assert completion
        assert all(
            x in completion for x in "--quiet --recursive --text".split()
        )

    @pytest.mark.complete("_grephelp -")
    def test_2(self, functions, completion):
        """Only long options should be included"""
        assert completion
        assert all(x.startswith("--") for x in completion)

    @pytest.mark.complete("_grephelp --")
    def test_3(self, functions, completion):
        """Should have both ones ending with a = and ones not"""
        assert completion
        assert any(x.endswith("=") for x in completion)
        assert any(not x.endswith("=") for x in completion)

    @pytest.mark.complete("_various --")
    def test_no_dashdashdash(self, functions, completion):
        assert all(not x.startswith("---") for x in completion)

    @pytest.mark.complete("_various --")
    def test_no_trailingdash(self, functions, completion):
        assert all(not x.endswith("-") for x in completion)

    @pytest.mark.complete("_various --")
    def test_underscore(self, functions, completion):
        assert "--foo_bar" in completion

    @pytest.mark.complete("_various --")
    def test_equals(self, functions, completion):
        assert "--foo=" in completion
