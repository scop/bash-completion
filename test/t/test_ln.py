import pytest


class TestLn(object):

    @pytest.mark.complete("ln ")
    def test_1(self, completion):
        assert completion.list
