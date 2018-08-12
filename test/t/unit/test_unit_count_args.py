import pytest

from conftest import assert_bash_exec


@pytest.mark.bashcomp(cmd=None, ignore_env=r"^\+args=")
class TestUnitCountArgs:

    def test_1(self, bash):
        assert_bash_exec(bash, "_count_args >/dev/null")
