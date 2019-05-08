import pytest


class TestPostfix:
    @pytest.mark.complete("postfix ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("postfix -")
    def test_2(self, completion):
        assert completion
