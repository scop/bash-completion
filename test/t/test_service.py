import sys

import pytest


class TestService:
    @pytest.mark.xfail(
        sys.platform == "darwin",
        reason="Service completion not available on macOS",
    )
    @pytest.mark.complete(
        "service ",
        # Skip if we don't have a way to find services
        skipif="! (type systemctl || type service || type initctl || "
        "[[ -d /etc/rc.d/init.d || "
        "-d /etc/init.d || "
        "-d /etc/xinetd.d || "
        "-f /etc/slackware-version ]])",
    )
    def test_1(self, completion):
        assert completion
