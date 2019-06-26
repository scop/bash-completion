import pytest


class TestSmbcquotas:
    @pytest.mark.complete("smbcquotas -", require_cmd=True)
    def test_1(self, completion):
        assert completion
