import pytest


class TestSftp:
    @pytest.mark.complete("sftp -Fsp", cwd="sftp")
    def test_1(self, completion):
        assert completion == "-Fspaced  conf"

    @pytest.mark.complete("sftp -")
    def test_2(self, completion):
        assert completion
