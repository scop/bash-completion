import pytest


class TestArpspoof:
    @pytest.mark.complete("arpspoof -")
    def test_1(self, completion):
        assert completion
