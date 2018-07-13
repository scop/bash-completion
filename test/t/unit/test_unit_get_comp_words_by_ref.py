import pytest

from conftest import assert_bash_exec


@pytest.mark.bashcomp(cmd=None, ignore_env=r"^\+cur=")
class TestUnitGetCompWordsByRef(object):

    def test_1(self, bash):
        assert_bash_exec(bash, "_get_comp_words_by_ref cur >/dev/null")
