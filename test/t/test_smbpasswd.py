import pytest


class TestSmbpasswd:
    @pytest.mark.complete("smbpasswd -")
    def test_1(self, completion):
        assert completion
