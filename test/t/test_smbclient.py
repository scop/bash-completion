import pytest


class TestSmbclient:
    @pytest.mark.complete("smbclient -", require_cmd=True)
    def test_1(self, completion):
        assert completion
