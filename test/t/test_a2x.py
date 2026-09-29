import pytest


class TestA2x:
    @pytest.mark.complete("a2x ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("a2x -", require_cmd=True)
    def test_2(self, completion):
        assert completion
