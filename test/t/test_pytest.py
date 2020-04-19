import pytest


class TestPytest:
    @pytest.mark.complete("pytest ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("pytest -")
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete("pytest ../t/test_pytest.py:")
    def test_classes(self, completion):
        assert len(completion) == 1
        assert next(iter(completion)).endswith("::TestPytest")
