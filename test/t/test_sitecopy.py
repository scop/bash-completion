import pytest


class Test(object):

    @pytest.mark.complete("sitecopy --")
    def test_dash(self, completion):
        assert completion.list
