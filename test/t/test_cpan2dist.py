import pytest


class Test(object):

    @pytest.mark.complete("cpan2dist -")
    def test_dash(self, completion):
        assert completion.list
