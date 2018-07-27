import pytest


class TestSha1sum:

    @pytest.mark.complete("sha1sum --")
    def test_1(self, completion):
        assert completion.list
