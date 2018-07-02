import pytest


class Test(object):

    @pytest.mark.complete("check_db -")
    def test_dash(self, completion):
        assert completion.list
