import os

import pytest


@pytest.mark.bashcomp(cmd="ether-wake")
class TestEtherWake:
    @pytest.mark.xfail(
        os.environ.get("NETWORK") == "none",
        reason="MAC addresses may be N/A with no networking configured",
    )
    @pytest.mark.complete("ether-wake ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("ether-wake -", require_cmd=True)
    def test_2(self, completion):
        assert completion
