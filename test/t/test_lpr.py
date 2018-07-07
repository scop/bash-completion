import pytest


class TestLpr(object):

    @pytest.mark.complete("lpr ")
    def test_1(self, completion):
        assert completion.list
