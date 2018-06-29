import pytest


class Test(object):

    @pytest.mark.complete("sbopkg -")
    def test_dash(self, completion):
        assert completion.list
