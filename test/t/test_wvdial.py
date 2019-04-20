import pytest


class TestWvdial:
    @pytest.mark.complete("wvdial -")
    def test_1(self, completion):
        assert completion
