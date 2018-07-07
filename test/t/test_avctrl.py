import pytest


class TestAvctrl(object):

    @pytest.mark.complete("avctrl ")
    def test_1(self, completion):
        assert completion.list
