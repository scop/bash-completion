import pytest


class TestHexdump:
    @pytest.mark.complete("hexdump -", require_cmd=True)
    def test_1(self, completion):
        assert completion
