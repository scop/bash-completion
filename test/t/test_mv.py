import pytest


class TestMv:
    @pytest.mark.complete("mv ")
    def test_1(self, completion):
        assert completion
