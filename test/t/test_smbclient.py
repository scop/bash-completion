import pytest


class TestSmbclient:
    @pytest.mark.complete("smbclient -")
    def test_1(self, completion):
        assert completion
