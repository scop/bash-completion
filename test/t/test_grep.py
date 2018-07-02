import pytest


class Test(object):

    @pytest.mark.complete("grep --")
    def test_dash(self, completion):
        assert completion.list
