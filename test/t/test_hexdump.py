import pytest


class TestHexdump:
    @pytest.mark.complete("hexdump -")
    def test_1(self, completion):
        assert completion
