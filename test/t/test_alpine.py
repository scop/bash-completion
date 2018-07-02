import pytest


class Test(object):

    @pytest.mark.complete("alpine -")
    def test_dash(self, completion):
        assert completion.list
