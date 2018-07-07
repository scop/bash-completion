import pytest


class TestLua(object):

    @pytest.mark.complete("lua ")
    def test_1(self, completion):
        assert completion.list
