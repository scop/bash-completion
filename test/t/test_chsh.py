import pytest


class TestChsh:
    @pytest.mark.complete("chsh ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("chsh -s ")
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete("chsh -", require_cmd=True)
    def test_3(self, completion):
        assert completion
