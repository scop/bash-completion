import pytest


class Test(object):

    @pytest.mark.complete("cal ")
    def test_(self, completion):
        assert completion.list
