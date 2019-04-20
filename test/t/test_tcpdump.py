import pytest


class TestTcpdump:
    @pytest.mark.complete("tcpdump -")
    def test_1(self, completion):
        assert completion
