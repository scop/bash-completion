import pytest


class TestCPlusPlus(object):

    @pytest.mark.complete("c++ ")
    def test_1(self, completion):
        assert completion.list
