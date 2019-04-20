import pytest


class TestRoute:
    @pytest.mark.complete("route ")
    def test_1(self, completion):
        assert completion
