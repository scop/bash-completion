import pytest


class TestLvextend(object):

    @pytest.mark.complete("lvextend --",
                          skipif="! lvextend --help &>/dev/null")
    def test_1(self, completion):
        assert completion.list
