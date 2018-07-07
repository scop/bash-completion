import pytest


class TestLvresize(object):

    @pytest.mark.complete("lvresize --",
                          skipif="! lvresize --help &>/dev/null")
    def test_1(self, completion):
        assert completion.list
