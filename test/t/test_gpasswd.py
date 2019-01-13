import pytest


class TestGpasswd:

    @pytest.mark.complete("gpasswd ")
    def test_1(self, completion):
        assert completion
