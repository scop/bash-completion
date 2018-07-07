import pytest


class TestWvdial(object):

    @pytest.mark.complete("wvdial -")
    def test_1(self, completion):
        assert completion.list
