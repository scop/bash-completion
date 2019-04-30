import pytest


class TestArp:
    @pytest.mark.complete("arp ", skipif='test -z "$(arp 2>/dev/null)"')
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("arp -")
    def test_2(self, completion):
        assert completion
