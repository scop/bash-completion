import pytest


class TestNtpdate:
    @pytest.mark.complete("ntpdate -", require_cmd=True)
    def test_1(self, completion):
        assert completion
