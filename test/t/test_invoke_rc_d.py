import sys

import pytest


@pytest.mark.bashcomp(cmd="invoke-rc.d")
class TestInvokeRcD:
    @pytest.mark.xfail(
        sys.platform == "darwin",
        reason="Service completion not available on macOS",
    )
    @pytest.mark.complete("invoke-rc.d ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("invoke-rc.d --no-fallback --")
    def test_2(self, completion):
        """Test already specified option is not offered."""
        if sys.platform != "darwin":  # no service completion
            assert completion
        assert "--no-fallback" not in completion
