import pytest


class Test(object):

    @pytest.mark.complete("pwgen -")
    def test_dash(self, completion):
        assert completion.list
