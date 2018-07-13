import pytest

from conftest import assert_bash_exec


@pytest.mark.bashcomp(cmd=None)
class TestUnitGetCword(object):

    def test_1(self, bash):
        assert_bash_exec(bash, "_get_cword >/dev/null")
