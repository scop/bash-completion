import pytest


class TestEtherWake(object):

    @pytest.mark.complete("ether-wake ")
    def test_1(self, completion):
        assert completion.list
