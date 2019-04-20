import pytest


class TestCut:
    @pytest.mark.complete("cut ")
    def test_1(self, completion):
        assert completion
