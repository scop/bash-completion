import pytest


class TestSshow:
    @pytest.mark.complete("sshow -")
    def test_1(self, completion):
        assert completion
