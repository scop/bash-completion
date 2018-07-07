import pytest


class TestArpspoof(object):

    @pytest.mark.complete("arpspoof -")
    def test_1(self, completion):
        assert completion.list
