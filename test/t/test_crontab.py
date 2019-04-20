import pytest


class TestCrontab:
    @pytest.mark.complete("crontab ")
    def test_1(self, completion):
        assert completion
