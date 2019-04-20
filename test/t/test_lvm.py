import pytest


class TestLvm:
    @pytest.mark.complete("lvm pv")
    def test_1(self, completion):
        assert completion
