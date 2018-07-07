import pytest


class TestCi(object):

    @pytest.mark.complete("ci ")
    def test_1(self, completion):
        assert completion.list
