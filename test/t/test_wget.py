import pytest


class TestWget:
    @pytest.mark.complete("wget ")
    def test_1(self, completion):
        assert not completion

    @pytest.mark.complete("wget --h")
    def test_2(self, completion):
        assert completion
