import pytest


class TestStrace:
    @pytest.mark.complete("strace -")
    def test_1(self, completion):
        assert completion
