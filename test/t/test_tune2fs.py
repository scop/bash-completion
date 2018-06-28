import pytest


class Test(object):

    @pytest.mark.complete("tune2fs ")
    def test_(self, completion):
        assert completion.list
