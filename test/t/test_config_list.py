import pytest


class Test(object):

    @pytest.mark.complete("config_list -")
    def test_dash(self, completion):
        assert completion.list
