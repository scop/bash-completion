import pytest


class TestRmmod(object):

    @pytest.mark.complete("rmmod -")
    def test_1(self, completion):
        assert completion.list
