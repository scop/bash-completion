import pytest


class TestPydoc:
    @pytest.mark.complete("pydoc r")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("pydoc -")
    def test_2(self, completion):
        assert completion
