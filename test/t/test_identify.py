import pytest


class Test(object):

    @pytest.mark.complete("identify -")
    def test_dash(self, completion):
        assert completion.list
