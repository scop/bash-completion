import pytest


class TestId:
    @pytest.mark.complete("id -")
    def test_1(self, completion):
        assert completion
