import pytest


class TestSmbtar:
    @pytest.mark.complete("smbtar -", require_cmd=True)
    def test_1(self, completion):
        assert completion
