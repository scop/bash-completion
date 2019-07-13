import pytest


class TestArp:
    @pytest.mark.complete(
        "arp ", require_cmd=True, skipif='test -z "$(arp 2>/dev/null)"'
    )
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("arp -", require_cmd=True)
    def test_2(self, completion):
        assert completion
