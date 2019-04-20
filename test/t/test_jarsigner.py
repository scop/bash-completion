import pytest


class TestJarsigner:
    @pytest.mark.complete("jarsigner ")
    def test_1(self, completion):
        assert completion
