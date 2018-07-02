import pytest


class Test(object):

    @pytest.mark.complete("chroot ")
    def test_(self, completion):
        assert completion.list
