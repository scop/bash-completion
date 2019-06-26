import pytest


class TestUrlsnarf:
    @pytest.mark.complete("urlsnarf -", require_cmd=True)
    def test_1(self, completion):
        assert completion
