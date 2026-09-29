import pytest

from conftest import assert_bash_exec


@pytest.mark.bashcomp(cmd=None, ignore_env=r"^\+(VAR=|declare -f foo)")
class TestUnlocal:
    def test_1(self, bash):
        cmd = (
            "foo() { "
            "local VAR=inner; "
            "_comp_unlocal VAR; "
            "echo $VAR; "
            "}; "
            "VAR=outer; foo; "
        )
        res = assert_bash_exec(bash, cmd, want_output=True).strip()
        assert res == "outer"
