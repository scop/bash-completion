import pytest


class Test(object):

    @pytest.mark.complete("arpspoof -")
    def test_dash(self, completion):
        assert completion.list
