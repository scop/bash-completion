import pytest


class TestHtop:
    @pytest.mark.complete("htop -", require_cmd=True)
    def test_1(self, completion):
        assert completion
