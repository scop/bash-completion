import pytest


class TestLvremove(object):

    @pytest.mark.complete("lvremove --",
                          skipif="! lvremove --help &>/dev/null")
    def test_1(self, completion):
        assert completion.list
