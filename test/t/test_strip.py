import pytest


class TestStrip:
    @pytest.mark.complete("strip --")
    def test_1(self, completion):
        assert completion
