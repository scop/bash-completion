import pytest

from conftest import TestUnitBase, assert_bash_exec


@pytest.mark.bashcomp(cmd=None)
class TestUnitQuote(TestUnitBase):
    def test_1(self, bash):
        output = assert_bash_exec(
            bash, 'quote "a b"', want_output=True, want_newline=False
        )
        assert output.strip() == "'a b'"

    def test_2(self, bash):
        output = assert_bash_exec(
            bash, 'quote "a  b"', want_output=True, want_newline=False
        )
        assert output.strip() == "'a  b'"

    def test_3(self, bash):
        output = assert_bash_exec(
            bash, 'quote "  a "', want_output=True, want_newline=False
        )
        assert output.strip() == "'  a '"

    def test_4(self, bash):
        output = assert_bash_exec(
            bash, "quote \"a'b'c\"", want_output=True, want_newline=False
        )
        assert output.strip() == r"'a'\''b'\''c'"

    def test_5(self, bash):
        output = assert_bash_exec(
            bash, 'quote "a\'"', want_output=True, want_newline=False
        )
        assert output.strip() == r"'a'\'''"
