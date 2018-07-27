import pytest


class TestPytest:

    @pytest.mark.complete("pytest ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("pytest -")
    def test_2(self, completion):
        assert completion.list
