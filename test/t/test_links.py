import pytest


class TestLinks:
    @pytest.mark.complete("links ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("links -", require_cmd=True)
    def test_2(self, completion):
        assert completion
