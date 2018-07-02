import pytest


class Test(object):

    @pytest.mark.complete("munin-run -")
    def test_dash(self, completion):
        assert completion.list
