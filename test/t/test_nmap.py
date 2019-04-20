import pytest


class TestNmap:
    @pytest.mark.complete("nmap --v")
    def test_1(self, completion):
        assert completion
