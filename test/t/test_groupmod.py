import pytest


class TestGroupmod(object):

    @pytest.mark.complete("groupmod ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("groupmod -")
    def test_2(self, completion):
        assert completion.list
