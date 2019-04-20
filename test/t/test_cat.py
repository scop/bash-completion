import pytest


class TestCat:
    @pytest.mark.complete("cat ")
    def test_1(self, completion):
        assert completion
