import pytest


class TestFbi:
    @pytest.mark.complete("fbi ")
    def test_1(self, completion):
        assert completion
