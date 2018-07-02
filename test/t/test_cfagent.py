import pytest


class Test(object):

    @pytest.mark.complete("cfagent -")
    def test_dash(self, completion):
        assert completion.list
