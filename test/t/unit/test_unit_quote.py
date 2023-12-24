import pytest

from conftest import TestUnitBase, assert_bash_exec


@pytest.mark.bashcomp(
    cmd=None,
    ignore_env=r"^\+declare -f __tester$",
)
class TestUnitQuote(TestUnitBase):
    def test_1(self, bash):
        assert_bash_exec(
            bash,
            '__tester() { local REPLY; _comp_quote "$1"; printf %s "$REPLY"; }',
        )
        output = assert_bash_exec(
            bash, '__tester "a b"', want_output=True, want_newline=False
        )
        assert output.strip() == "'a b'"

    def test_2(self, bash):
        output = assert_bash_exec(
            bash, '__tester "a  b"', want_output=True, want_newline=False
        )
        assert output.strip() == "'a  b'"

    def test_3(self, bash):
        output = assert_bash_exec(
            bash, '__tester "  a "', want_output=True, want_newline=False
        )
        assert output.strip() == "'  a '"

    def test_4(self, bash):
        output = assert_bash_exec(
            bash, "__tester \"a'b'c\"", want_output=True, want_newline=False
        )
        assert output.strip() == r"'a'\''b'\''c'"

    def test_5(self, bash):
        output = assert_bash_exec(
            bash, '__tester "a\'"', want_output=True, want_newline=False
        )
        assert output.strip() == r"'a'\'''"
