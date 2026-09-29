import pytest


class TestChpasswd:
    @pytest.mark.complete("chpasswd -", require_cmd=True)
    def test_1(self, completion):
        assert completion
