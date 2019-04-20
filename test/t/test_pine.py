import pytest


class TestPine:
    @pytest.mark.complete("pine -")
    def test_1(self, completion):
        assert completion
