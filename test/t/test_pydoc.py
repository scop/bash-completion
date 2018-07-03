import pytest


class Test(object):

    @pytest.mark.complete("pydoc r")
    def test_r(self, completion):
        assert completion.list
