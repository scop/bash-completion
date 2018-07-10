import pytest


class TestSsh(object):

    @pytest.mark.complete("ssh -Fsp", cwd="ssh")
    def test_1(self, completion):
        assert completion.list == ["-Fspaced  conf"]
