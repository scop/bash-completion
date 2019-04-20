import pytest


class TestIonice:
    @pytest.mark.complete("ionice -")
    def test_1(self, completion):
        assert completion
