import pytest


class TestNewusers:
    @pytest.mark.complete("newusers ")
    def test_1(self, completion):
        assert completion
