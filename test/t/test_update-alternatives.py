import pytest


class Test(object):

    @pytest.mark.complete("update-alternatives --")
    def test_dash(self, completion):
        assert completion.list
