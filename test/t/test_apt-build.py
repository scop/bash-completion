import pytest


class Test(object):

    @pytest.mark.complete("apt-build ")
    def test_(self, completion):
        assert completion.list
