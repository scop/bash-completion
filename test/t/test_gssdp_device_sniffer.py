import pytest


@pytest.mark.bashcomp(
    cmd="gssdp-device-sniffer",
)
class TestGssdpDeviceSniffer:
    @pytest.mark.complete("gssdp-device-sniffer ")
    def test_basic(self, completion):
        assert not completion

    @pytest.mark.complete("gssdp-device-sniffer -", require_cmd=True)
    def test_options(self, completion):
        assert "--help" in completion
