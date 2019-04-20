import pytest


class TestWatch:
    @pytest.mark.complete("watch -")
    def test_1(self, completion):
        assert completion
