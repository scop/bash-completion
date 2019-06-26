import pytest


class TestAlpine:
    @pytest.mark.complete("alpine -", require_cmd=True)
    def test_1(self, completion):
        assert completion
