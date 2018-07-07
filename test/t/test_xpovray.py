import pytest


class TestXpovray(object):

    @pytest.mark.complete("xpovray ")
    def test_1(self, completion):
        assert completion.list
