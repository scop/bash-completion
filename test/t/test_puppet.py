import pytest


class TestPuppet(object):

    @pytest.mark.complete("puppet ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("puppet agent --")
    def test_2(self, completion):
        assert completion.list
