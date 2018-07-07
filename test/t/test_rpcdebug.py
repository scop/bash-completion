import pytest


class TestRpcdebug(object):

    @pytest.mark.complete("rpcdebug -")
    def test_1(self, completion):
        assert completion.list
