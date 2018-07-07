import pytest


class TestKoji(object):

    @pytest.mark.complete("koji ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("koji -")
    def test_2(self, completion):
        assert completion.list
