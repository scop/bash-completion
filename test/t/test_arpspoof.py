import pytest


class TestArpspoof:
    @pytest.mark.complete("arpspoof -", require_cmd=True)
    def test_1(self, completion):
        assert completion
