import pytest


class TestPyston:
    @pytest.mark.complete("pyston ")
    def test_basic(self, completion):
        assert completion

    @pytest.mark.complete("pyston -")
    def test_options(self, completion):
        assert completion
