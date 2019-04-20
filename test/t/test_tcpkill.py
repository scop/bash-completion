import pytest


class TestTcpkill:
    @pytest.mark.complete("tcpkill -")
    def test_1(self, completion):
        assert completion
