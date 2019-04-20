import pytest


class TestLisp:
    @pytest.mark.complete("lisp ")
    def test_1(self, completion):
        assert completion
