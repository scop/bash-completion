import pytest


class Test(object):

    # Assume at least munin* available
    @pytest.mark.complete("munindoc m")
    def test_m(self, completion):
        assert completion.list
