import pytest


class TestRmlist:
    @pytest.mark.complete("rmlist -")
    def test_1(self, completion):
        assert completion
