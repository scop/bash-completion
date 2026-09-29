import pytest


class TestTcpdump:
    @pytest.mark.complete("tcpdump -", require_cmd=True)
    def test_1(self, completion):
        assert completion
