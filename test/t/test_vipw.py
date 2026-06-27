import pytest


class TestVipw:
    @pytest.mark.complete("vipw -", require_cmd=True)
    def test_1(self, completion):
        assert completion
