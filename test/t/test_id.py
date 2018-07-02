import pytest


class Test(object):

    @pytest.mark.complete("id -")
    def test_dash(self, completion):
        assert completion.list
