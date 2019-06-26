import pytest


class TestL2ping:
    @pytest.mark.complete("l2ping -", require_cmd=True)
    def test_1(self, completion):
        assert completion
