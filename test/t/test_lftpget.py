import pytest


class TestLftpget:
    @pytest.mark.complete("lftpget -")
    def test_1(self, completion):
        assert completion
