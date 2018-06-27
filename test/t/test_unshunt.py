import pytest


class Test(object):

    @pytest.mark.complete("unshunt --")
    def test_dash(self, completion):
        assert completion.list
