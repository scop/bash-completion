import pytest


class TestMkinitrd:
    @pytest.mark.complete("mkinitrd ")
    def test_1(self, completion):
        assert completion
