import pytest


class Test(object):

    @pytest.mark.complete("filesnarf -")
    def test_dash(self, completion):
        assert completion.list
