import pytest


class TestMsgsnarf:
    @pytest.mark.complete("msgsnarf -", require_cmd=True)
    def test_1(self, completion):
        assert completion
