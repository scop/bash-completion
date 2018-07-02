import pytest


class Test(object):

    @pytest.mark.complete("sync_members --")
    def test_dash(self, completion):
        assert completion.list
