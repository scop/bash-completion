import pytest


class Test(object):

    @pytest.mark.complete("bash --")
    def test_dash(self, completion):
        assert completion.list
