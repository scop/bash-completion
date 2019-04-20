import pytest


class TestSmbcquotas:
    @pytest.mark.complete("smbcquotas -")
    def test_1(self, completion):
        assert completion
