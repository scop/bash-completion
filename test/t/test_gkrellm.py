import os

import pytest


@pytest.mark.xfail(not os.environ.get("DISPLAY"), reason="X display required")
class TestGkrellm:
    @pytest.mark.complete("gkrellm -", require_cmd=True)
    def test_1(self, completion):
        assert completion
