import pytest


class Test(object):

    @pytest.mark.complete("yum-arch -")
    def test_dash(self, completion):
        assert completion.list
