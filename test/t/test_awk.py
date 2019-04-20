import pytest


class TestAwk:
    @pytest.mark.complete("awk ")
    def test_1(self, completion):
        assert completion
