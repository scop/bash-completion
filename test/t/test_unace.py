import pytest


class TestUnace:
    @pytest.mark.complete("unace -")
    def test_1(self, completion):
        assert completion
