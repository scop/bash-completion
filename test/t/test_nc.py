import pytest


class TestNc:
    @pytest.mark.complete("nc -", require_cmd=True)
    def test_1(self, completion):
        assert completion
