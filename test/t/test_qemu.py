import pytest


class Test(object):

    @pytest.mark.complete("qemu ")
    def test_(self, completion):
        assert completion.list
