import pytest


class TestCivserver(object):

    @pytest.mark.complete("civserver -")
    def test_1(self, completion):
        assert completion.list
