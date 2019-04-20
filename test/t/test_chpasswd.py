import pytest


class TestChpasswd:
    @pytest.mark.complete("chpasswd -")
    def test_1(self, completion):
        assert completion
