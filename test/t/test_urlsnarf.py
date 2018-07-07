import pytest


class TestUrlsnarf(object):

    @pytest.mark.complete("urlsnarf -")
    def test_1(self, completion):
        assert completion.list
