import pytest


class TestWatch:
    @pytest.mark.complete("watch -", require_cmd=True)
    def test_1(self, completion):
        assert completion
