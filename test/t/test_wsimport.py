import pytest


class TestWsimport(object):

    @pytest.mark.complete("wsimport ")
    def test_1(self, completion):
        assert completion.list
