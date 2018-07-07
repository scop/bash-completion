import pytest


class TestRrdtool(object):

    @pytest.mark.complete("rrdtool ")
    def test_1(self, completion):
        assert completion.list
