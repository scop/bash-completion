import pytest


class TestLilo:
    @pytest.mark.complete("lilo -")
    def test_1(self, completion):
        assert completion
