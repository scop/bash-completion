import pytest


class TestBash(object):

    @pytest.mark.complete("bash --")
    def test_1(self, completion):
        assert completion.list
