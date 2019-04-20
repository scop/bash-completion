import pytest


class TestSort:
    @pytest.mark.complete("sort --")
    def test_1(self, completion):
        assert completion
