import pytest

from conftest import assert_bash_exec, assert_complete


class TestRdesktop:
    @pytest.mark.complete("rdesktop -", require_cmd=True)
    def test_1(self, completion):
        assert completion

    def test_options_strip_colon(self, bash):
        assert_bash_exec(
            bash,
            "rdesktop() { printf '%s\\n' '   -u: user name' '   -k: keyboard layout'; }",
        )
        completion = assert_complete(bash, "rdesktop -")
        assert_bash_exec(bash, "unset -f rdesktop")
        assert completion == ["-k", "-u"]

    def test_options_no_help(self, bash):
        assert_bash_exec(bash, "rdesktop() { :; }")
        completion = assert_complete(bash, "rdesktop -")
        assert_bash_exec(bash, "unset -f rdesktop")
        assert not completion
