import pytest


class Test(object):

    @pytest.mark.complete("smartctl --")
    def test_dash(self, completion):
        assert completion.list
