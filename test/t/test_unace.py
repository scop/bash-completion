import pytest


class TestUnace(object):

    @pytest.mark.complete("unace -")
    def test_1(self, completion):
        assert completion.list
