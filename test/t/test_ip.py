import pytest


class TestIp(object):

    @pytest.mark.complete("ip ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("ip a ")
    def test_2(self, completion):
        assert completion.list
