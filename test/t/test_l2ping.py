import pytest


class TestL2ping(object):

    @pytest.mark.complete("l2ping -")
    def test_1(self, completion):
        assert completion.list
