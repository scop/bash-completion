import pytest


class TestDf(object):

    @pytest.mark.complete("df ")
    def test_1(self, completion):
        assert completion.list
