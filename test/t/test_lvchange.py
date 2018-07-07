import pytest


class TestLvchange(object):

    @pytest.mark.complete("lvchange --",
                          skipif="! lvchange --help &>/dev/null")
    def test_1(self, completion):
        assert completion.list
