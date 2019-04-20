import pytest


class TestVipw:
    @pytest.mark.complete("vipw -")
    def test_1(self, completion):
        assert completion
