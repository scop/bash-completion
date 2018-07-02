import pytest


class Test(object):

    @pytest.mark.complete("mmsitepass -")
    def test_dash(self, completion):
        assert completion.list
