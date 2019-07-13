import pytest


class TestHostname:
    @pytest.mark.complete("hostname -", require_cmd=True)
    def test_1(self, completion):
        assert completion
