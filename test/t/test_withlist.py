import pytest


class TestWithlist:
    @pytest.mark.complete("withlist --")
    def test_1(self, completion):
        assert completion
