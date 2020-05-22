import pytest


class TestArpspoof:
    @pytest.mark.complete(
        "arpspoof -",
        require_cmd=True,
        # May require privileges even for outputting the usage message
        skipif="arpspoof 2>&1 | command grep -qF libnet_open_link",
    )
    def test_1(self, completion):
        assert completion
