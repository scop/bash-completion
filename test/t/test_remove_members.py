import pytest


class Test(object):

    @pytest.mark.complete("remove_members --")
    def test_dash(self, completion):
        assert completion.list
