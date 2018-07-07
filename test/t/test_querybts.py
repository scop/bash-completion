import pytest


class TestQuerybts(object):

    @pytest.mark.complete("querybts --")
    def test_1(self, completion):
        assert completion.list
