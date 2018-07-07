import pytest


class TestVipw(object):

    @pytest.mark.complete("vipw -")
    def test_1(self, completion):
        assert completion.list
