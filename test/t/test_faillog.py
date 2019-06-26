import pytest


class TestFaillog:
    @pytest.mark.complete("faillog -", require_cmd=True)
    def test_1(self, completion):
        assert completion
