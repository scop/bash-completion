import pytest


class TestTcpnice:
    @pytest.mark.complete("tcpnice -")
    def test_1(self, completion):
        assert completion
