import pytest


class TestNtpdate:
    @pytest.mark.complete("ntpdate -")
    def test_1(self, completion):
        assert completion
