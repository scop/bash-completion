import pytest


class Test(object):

    @pytest.mark.complete("medusa -")
    def test_dash(self, completion):
        assert completion.list
