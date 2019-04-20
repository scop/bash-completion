import pytest


class TestClisp:
    @pytest.mark.complete("clisp ")
    def test_1(self, completion):
        assert completion
