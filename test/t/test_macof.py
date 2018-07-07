import pytest


class TestMacof(object):

    @pytest.mark.complete("macof -")
    def test_1(self, completion):
        assert completion.list
