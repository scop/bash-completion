import pytest


class TestLzip(object):

    @pytest.mark.complete("lzip ")
    def test_1(self, completion):
        assert completion.list
