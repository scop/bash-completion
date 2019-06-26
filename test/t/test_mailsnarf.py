import pytest


class TestMailsnarf:
    @pytest.mark.complete("mailsnarf -", require_cmd=True)
    def test_1(self, completion):
        assert completion
