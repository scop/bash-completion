import pytest


class TestChflags:
    @pytest.mark.complete("chflags no")
    def test_basic(self, completion):
        assert completion

    @pytest.mark.complete("chflags -")
    def test_basic(self, completion):
        assert completion and "-P" not in completion

    @pytest.mark.complete("chflags -R -")
    def test_basic(self, completion):
        assert "-P" in completion

    @pytest.mark.complete("chflags -v sappend ")
    def test_basic(self, completion):
        assert completion

