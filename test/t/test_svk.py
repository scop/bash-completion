import pytest


class TestSvk:
    @pytest.mark.complete("svk ")
    def test_1(self, completion):
        assert completion
