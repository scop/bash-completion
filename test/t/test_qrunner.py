import pytest


class Test(object):

    @pytest.mark.complete("qrunner -")
    def test_dash(self, completion):
        assert completion.list
