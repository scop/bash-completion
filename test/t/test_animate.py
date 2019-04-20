import pytest


class TestAnimate:
    @pytest.mark.complete("animate ")
    def test_1(self, completion):
        assert completion
