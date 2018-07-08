import pytest


class TestGPlusPlus(object):

    @pytest.mark.complete("g++ ")
    def test_1(self, completion):
        assert completion.list
