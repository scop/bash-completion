import pytest


class TestTee(object):

    @pytest.mark.complete("tee ")
    def test_1(self, completion):
        assert completion.list
