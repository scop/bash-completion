import pytest


class TestSmbcacls:
    @pytest.mark.complete("smbcacls -", require_cmd=True)
    def test_1(self, completion):
        assert completion
