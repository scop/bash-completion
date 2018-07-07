import pytest


class TestLess(object):

    @pytest.mark.complete("less --")
    def test_1(self, completion):
        assert completion.list
