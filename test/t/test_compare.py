import pytest


class TestCompare(object):

    @pytest.mark.complete("compare ")
    def test_1(self, completion):
        assert completion.list
