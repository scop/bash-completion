import pytest


class TestPyflakes:
    @pytest.mark.complete("pyflakes ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("pyflakes -")
    def test_2(self, completion):
        assert completion
