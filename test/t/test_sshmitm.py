import pytest


class Test(object):

    @pytest.mark.complete("sshmitm -")
    def test_dash(self, completion):
        assert completion.list
