import pytest


class TestQrunner:
    @pytest.mark.complete("qrunner -")
    def test_1(self, completion):
        assert completion
