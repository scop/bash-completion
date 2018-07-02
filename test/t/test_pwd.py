import pytest


class Test(object):

    @pytest.mark.complete("pwd -")
    def test_dash(self, completion):
        assert completion.list
