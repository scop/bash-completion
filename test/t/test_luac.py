import pytest


class TestLuac(object):

    @pytest.mark.complete("luac ")
    def test_1(self, completion):
        assert completion.list
