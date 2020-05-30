import inspect

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

    @pytest.mark.complete("pytest ../t/test_pytest.py::TestPytest::")
    def test_class_methods(self, completion):
        methods = inspect.getmembers(self, predicate=inspect.ismethod)
        assert len(completion) == len(methods)
        assert completion == [x[0] for x in methods]
