import pytest


class Test(object):

    @pytest.mark.complete("mysqladmin -")
    def test_dash(self, completion):
        assert completion.list
