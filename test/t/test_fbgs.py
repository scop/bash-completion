import pytest


class TestFbgs:
    @pytest.mark.complete("fbgs ")
    def test_1(self, completion):
        assert completion
