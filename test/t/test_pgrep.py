import pytest


class Test(object):

    # "p": Assume that our process name completion runs ps
    @pytest.mark.complete("pgrep p")
    def test_p(self, completion):
        assert completion.list
