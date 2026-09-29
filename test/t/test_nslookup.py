import pytest


class TestNslookup:
    @pytest.mark.complete("nslookup -")
    def test_1(self, completion):
        assert completion
