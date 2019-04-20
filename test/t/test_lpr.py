import pytest


class TestLpr:
    @pytest.mark.complete("lpr ")
    def test_1(self, completion):
        assert completion
