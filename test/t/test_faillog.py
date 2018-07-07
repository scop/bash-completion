import pytest


class TestFaillog(object):

    @pytest.mark.complete("faillog -")
    def test_1(self, completion):
        assert completion.list
