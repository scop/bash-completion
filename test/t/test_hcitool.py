import pytest


class TestHcitool:
    @pytest.mark.complete("hcitool ")
    def test_1(self, completion):
        assert completion
