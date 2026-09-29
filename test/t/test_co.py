import pytest


class TestCo:
    @pytest.mark.complete("co ")
    def test_1(self, completion):
        assert completion
