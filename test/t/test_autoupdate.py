import pytest


class TestAutoupdate:
    @pytest.mark.complete("autoupdate ")
    def test_1(self, completion):
        assert completion
