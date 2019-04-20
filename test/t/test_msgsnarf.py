import pytest


class TestMsgsnarf:
    @pytest.mark.complete("msgsnarf -")
    def test_1(self, completion):
        assert completion
