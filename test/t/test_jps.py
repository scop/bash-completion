import pytest


class TestJps(object):

    @pytest.mark.complete("jps -")
    def test_1(self, completion):
        assert completion.list
