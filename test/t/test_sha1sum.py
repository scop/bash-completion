import pytest


class TestSha1sum(object):

    @pytest.mark.complete("sha1sum --")
    def test_1(self, completion):
        assert completion.list
