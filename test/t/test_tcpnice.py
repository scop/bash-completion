import pytest


class TestTcpnice:
    @pytest.mark.complete("tcpnice -", require_cmd=True)
    def test_1(self, completion):
        assert completion
