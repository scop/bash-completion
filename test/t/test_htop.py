import pytest


class TestHtop(object):

    @pytest.mark.complete("htop -")
    def test_1(self, completion):
        assert completion.list
