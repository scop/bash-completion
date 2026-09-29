import pytest


class TestSmbpasswd:
    @pytest.mark.complete("smbpasswd -", require_cmd=True)
    def test_1(self, completion):
        assert completion
