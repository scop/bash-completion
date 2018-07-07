import pytest


class TestCut(object):

    @pytest.mark.complete("cut ")
    def test_1(self, completion):
        assert completion.list
