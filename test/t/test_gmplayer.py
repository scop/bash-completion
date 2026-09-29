import pytest


class TestGmplayer:
    @pytest.mark.complete("gmplayer ")
    def test_1(self, completion):
        assert completion
