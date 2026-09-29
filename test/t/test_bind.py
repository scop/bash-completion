import pytest


class TestBind:
    @pytest.mark.complete("bind -", require_cmd=True)
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("bind k")
    def test_2(self, completion):
        assert completion
