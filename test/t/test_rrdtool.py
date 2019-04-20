import pytest


class TestRrdtool:
    @pytest.mark.complete("rrdtool ")
    def test_1(self, completion):
        assert completion
