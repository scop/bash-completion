import pytest


class TestSu:
    @pytest.mark.complete("su ")
    def test_1(self, completion):
        assert completion
