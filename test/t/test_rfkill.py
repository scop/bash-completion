import pytest


class TestRfkill(object):

    @pytest.mark.complete("rfkill ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("rfkill -")
    def test_2(self, completion):
        assert completion.list
