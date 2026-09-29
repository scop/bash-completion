import pytest


class TestMc:
    @pytest.mark.complete("mc -", require_cmd=True)
    def test_1(self, completion):
        assert completion
