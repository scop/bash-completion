import pytest


class Test(object):

    @pytest.mark.complete("udevadm ")
    def test_(self, completion):
        assert completion.list
