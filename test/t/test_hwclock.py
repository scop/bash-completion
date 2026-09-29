import pytest


class TestHwclock:
    @pytest.mark.complete("hwclock -", require_cmd=True)
    def test_1(self, completion):
        assert completion
