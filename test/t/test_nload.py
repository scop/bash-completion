import pytest


class TestNload:
    @pytest.mark.complete("nload ")
    def test_basic(self, completion):
        assert completion

    @pytest.mark.complete("nload -", require_cmd=True)
    def test_options(self, completion):
        assert completion
