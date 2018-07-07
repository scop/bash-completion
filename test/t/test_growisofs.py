import pytest


class TestGrowisofs(object):

    @pytest.mark.complete("growisofs ")
    def test_1(self, completion):
        assert completion.list
