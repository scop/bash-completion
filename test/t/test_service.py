import sys

import pytest


class TestService:
    @pytest.mark.xfail(
        sys.platform == "darwin",
        reason="Service completion not available on macOS",
    )
    @pytest.mark.complete("service ")
    def test_1(self, completion):
        assert completion
