import pytest


class TestPostmap:
    @pytest.mark.complete("postmap ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("postmap -", require_cmd=True)
    def test_2(self, completion):
        assert completion
