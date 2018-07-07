import pytest


class TestSpovray(object):

    @pytest.mark.complete("spovray ")
    def test_1(self, completion):
        assert completion.list
