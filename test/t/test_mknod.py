import pytest


class Test(object):

    @pytest.mark.complete("mknod ")
    def test_(self, completion):
        assert completion.list
