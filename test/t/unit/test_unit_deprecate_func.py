import pytest

from conftest import assert_bash_exec


@pytest.mark.bashcomp(cmd=None, ignore_env=r"^\+declare -f func[12]$")
class TestUnitDeprecateFunc:
    def test_1(self, bash):
        assert_bash_exec(
            bash,
            'func1() { echo "func1($*)"; }; '
            "_comp_deprecate_func 2.12 func2 func1",
        )
        output = assert_bash_exec(bash, "func2 1 2 3", want_output=True)
        assert output.strip() == "func1(1 2 3)"
