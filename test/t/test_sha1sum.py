import pytest


class Test(object):

    @pytest.mark.complete("sha1sum --")
    def test_dash(self, completion):
        assert completion.list
