import pytest


class TestChflags:
    @pytest.mark.complete("chflags no")
    def test_basic(self, completion):
        assert completion

    @pytest.mark.complete("chflags -")
    def test_options(self, completion):
        assert completion and "-P" not in completion

    @pytest.mark.complete("chflags -R -")
    def test_options_after_R(self, completion):
        assert "-P" in completion

    @pytest.mark.complete("chflags -v sappend ")
    def test_first_word(self, completion):
        assert completion
