import pytest


class TestStrace:
    @pytest.mark.complete("strace -", require_cmd=True)
    def test_1(self, completion):
        assert completion
