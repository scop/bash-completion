import pytest


class TestJavac:
    @pytest.mark.complete("javac ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("javac -cp java/")
    def test_2(self, completion):
        assert completion == "a/ bashcomp.jar".split()
