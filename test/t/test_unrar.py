import pytest


class Test(object):

    @pytest.mark.complete("unrar -")
    def test_dash(self, completion):
        assert completion.list
