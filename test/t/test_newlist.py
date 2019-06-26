import pytest


class TestNewlist:
    @pytest.mark.complete("newlist -", require_cmd=True)
    def test_1(self, completion):
        assert completion
