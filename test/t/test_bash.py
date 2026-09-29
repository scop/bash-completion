import pytest


class TestBash:
    @pytest.mark.complete("bash --", require_cmd=True)
    def test_1(self, completion):
        assert completion
