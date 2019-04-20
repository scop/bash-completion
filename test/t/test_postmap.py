import pytest


class TestPostmap:
    @pytest.mark.complete("postmap ")
    def test_1(self, completion):
        assert completion
