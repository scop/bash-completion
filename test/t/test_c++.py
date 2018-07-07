import pytest


class TestC++(object):

    @pytest.mark.complete("c++ ")
    def test_1(self, completion):
        assert completion.list
