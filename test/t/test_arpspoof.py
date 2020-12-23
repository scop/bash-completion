import pytest


class TestArpspoof:
    @pytest.mark.complete(
        "arpspoof -",
        require_cmd=True,
        # May require privileges or network interfaces available even for
        # outputting the usage message. Unfortunately --help provokes a
        # non-zero exit status so we cannot test for that.
        skipif=(
            "arpspoof 2>&1 | "
            "command grep -qE 'libnet_(open_link|select_device)'"
        ),
    )
    def test_1(self, completion):
        assert completion
