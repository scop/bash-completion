import pytest


class TestHping3:
    @pytest.mark.complete("hping3 ")
    def test_1(self, completion):
        assert completion
