import pytest


class Test(object):

    @pytest.mark.complete("mkinitrd ")
    def test_(self, completion):
        assert completion.list
