import pytest


class TestLastlog:
    @pytest.mark.complete("lastlog -", require_cmd=True)
    def test_1(self, completion):
        assert completion
