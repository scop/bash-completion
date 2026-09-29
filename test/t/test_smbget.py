import pytest


class TestSmbget:
    @pytest.mark.complete("smbget -", require_cmd=True)
    def test_1(self, completion):
        assert completion
