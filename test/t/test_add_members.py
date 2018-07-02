import pytest


class Test(object):

    @pytest.mark.complete("add_members -")
    def test_dash(self, completion):
        assert completion.list
