import pytest


class TestLd:
    @pytest.mark.complete("ld ")
    def test_1(self, completion):
        assert completion
