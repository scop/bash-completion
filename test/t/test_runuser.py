import pytest


class TestRunuser:
    @pytest.mark.complete("runuser ")
    def test_1(self, completion):
        assert completion
