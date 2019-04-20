import pytest


class TestSmbtar:
    @pytest.mark.complete("smbtar -")
    def test_1(self, completion):
        assert completion
