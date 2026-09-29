import pytest


class TestGpc:
    @pytest.mark.complete("gpc ")
    def test_1(self, completion):
        assert completion
