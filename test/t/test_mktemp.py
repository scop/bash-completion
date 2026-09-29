import pytest


class TestMktemp:
    @pytest.mark.complete("mktemp -")
    def test_1(self, completion):
        assert completion
