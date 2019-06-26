import pytest


class TestGpasswd:
    @pytest.mark.complete("gpasswd ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("gpasswd -", require_cmd=True)
    def test_2(self, completion):
        assert completion
