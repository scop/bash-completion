import pytest


class TestP4:
    @pytest.mark.complete("p4 ")
    def test_1(self, completion):
        assert completion
