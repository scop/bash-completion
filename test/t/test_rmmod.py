import pytest


class TestRmmod:
    @pytest.mark.complete("rmmod -", require_cmd=True)
    def test_1(self, completion):
        assert completion
