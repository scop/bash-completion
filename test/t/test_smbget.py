import pytest


class TestSmbget:
    @pytest.mark.complete("smbget -")
    def test_1(self, completion):
        assert completion
