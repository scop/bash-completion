import pytest


class Test(object):

    @pytest.mark.complete("iperf ")
    def test_(self, completion):
        assert completion.list

    @pytest.mark.complete("iperf --bind ")
    def test_bind(self, completion):
        assert completion.list
