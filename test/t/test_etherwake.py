import pytest


class TestEtherwake(object):

    @pytest.mark.complete("etherwake -")
    def test_1(self, completion):
        assert completion.list
