import pytest


class TestCsplit:
    @pytest.mark.complete("csplit ")
    def test_1(self, completion):
        assert completion
