import inspect

import pytest


class TestPytest:
    @pytest.mark.complete("pytest ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("pytest -", require_cmd=True)
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete("pytest ../t/test_pytest.py:")
    def test_classes_and_functions(self, completion):
        assert completion == ":TestPytest :test_function_canary".split()

    @pytest.mark.complete("pytest ../t/test_pytest.py::TestPytest::")
    def test_class_methods(self, completion):
        methods = [
            x[0]
            for x in inspect.getmembers(self, predicate=inspect.ismethod)
            if x[0].startswith("test_")
        ]
        assert completion == methods

    @pytest.mark.complete("pytest pytest/test_async.py:")
    def test_classes_and_async_functions(self, completion):
        assert completion == ":Testing :test_positive".split()

    @pytest.mark.complete("pytest pytest/test_async.py::Testing::")
    def test_async_class_methods(self, completion):
        assert completion == "test_positive"

    def non_test_cananary_method(self):
        pass


def test_function_canary():
    pass


def non_test_canary():
    pass


class NonTestCanaryClass:
    def test_is_this_function_not(self):
        pass
