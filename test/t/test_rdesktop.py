import pytest


class Test(object):

    @pytest.mark.complete("rdesktop -")
    def test_dash(self, completion):
        assert completion.list
