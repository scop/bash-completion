import pytest


class Test(object):

    @pytest.mark.complete("bc --")
    def test_dash(self, completion):
        assert completion.list
