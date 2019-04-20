import pytest


class TestTightvncviewer:
    @pytest.mark.complete("tightvncviewer ")
    def test_1(self, completion):
        assert completion
