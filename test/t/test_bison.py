import pytest


class TestBison:
    @pytest.mark.complete("bison --")
    def test_1(self, completion):
        assert completion
