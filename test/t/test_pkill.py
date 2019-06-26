import pytest


class TestPkill:
    @pytest.mark.complete("pkill ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("pkill -", require_cmd=True)
    def test_2(self, completion):
        assert completion
