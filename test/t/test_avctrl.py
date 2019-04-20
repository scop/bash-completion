import pytest


class TestAvctrl:
    @pytest.mark.complete("avctrl ")
    def test_1(self, completion):
        assert completion
