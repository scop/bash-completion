import pytest


class Test(object):

    @pytest.mark.complete("minicom -")
    def test_dash(self, completion):
        assert completion.list
