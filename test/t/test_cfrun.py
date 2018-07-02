import pytest


class Test(object):

    @pytest.mark.complete("cfrun -")
    def test_dash(self, completion):
        assert completion.list
