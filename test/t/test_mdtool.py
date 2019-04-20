import pytest


class TestMdtool:
    @pytest.mark.complete("mdtool ")
    def test_1(self, completion):
        assert completion
