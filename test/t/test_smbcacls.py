import pytest


class TestSmbcacls:
    @pytest.mark.complete("smbcacls -")
    def test_1(self, completion):
        assert completion
