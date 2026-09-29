import pytest


class TestKplayer:
    @pytest.mark.complete("kplayer ")
    def test_1(self, completion):
        assert completion
