import pytest


class Test(object):

    @pytest.mark.complete("complete -")
    def test_dash(self, completion):
        assert completion.list
