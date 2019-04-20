import pytest


class TestNsupdate:
    @pytest.mark.complete("nsupdate ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("nsupdate -")
    def test_2(self, completion):
        assert completion
