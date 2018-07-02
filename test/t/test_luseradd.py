import pytest


class Test(object):

    @pytest.mark.complete("luseradd -")
    def test_dash(self, completion):
        assert completion.list
