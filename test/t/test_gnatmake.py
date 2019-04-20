import pytest


class TestGnatmake:
    @pytest.mark.complete("gnatmake ")
    def test_1(self, completion):
        assert completion
