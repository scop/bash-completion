import pytest


class TestWvdial:
    @pytest.mark.complete("wvdial -", require_cmd=True)
    def test_1(self, completion):
        assert completion
