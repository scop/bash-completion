import pytest


class TestPhing(object):

    @pytest.mark.complete("phing -")
    def test_1(self, completion):
        assert completion.list
