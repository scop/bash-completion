import pytest


class TestLpq(object):

    @pytest.mark.complete("lpq ")
    def test_1(self, completion):
        assert completion.list
