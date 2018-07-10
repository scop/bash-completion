import pytest


class TestSftp(object):

    @pytest.mark.complete("sftp -Fsp", cwd="sftp")
    def test_1(self, completion):
        assert completion.list == ["-Fspaced  conf"]
