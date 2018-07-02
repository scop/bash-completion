import pytest


class Test(object):

    @pytest.mark.complete("enscript --")
    def test_dash(self, completion):
        assert completion.list
