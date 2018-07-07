import pytest


class TestPlagueClient(object):

    @pytest.mark.complete("plague-client ")
    def test_1(self, completion):
        assert completion.list
