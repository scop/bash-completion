import pytest


class TestHwclock:
    @pytest.mark.complete("hwclock -")
    def test_1(self, completion):
        assert completion
