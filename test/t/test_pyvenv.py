import pytest


class TestPyvenv:
    @pytest.mark.complete("pyvenv ")
    def test_1(self, completion):
        assert completion
