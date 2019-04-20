import pytest


class TestAlpine:
    @pytest.mark.complete("alpine -")
    def test_1(self, completion):
        assert completion
