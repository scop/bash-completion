import pytest


class TestJavac:

    @pytest.mark.complete("javac ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("javac -cp java/")
    def test_2(self, completion):
        assert completion.list == "a/ bashcomp.jar".split()
