import pytest


class Test(object):

    @pytest.mark.complete("host -")
    def test_dash(self, completion):
        assert completion.list
