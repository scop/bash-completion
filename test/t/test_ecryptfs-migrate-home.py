import pytest


class Test(object):

    @pytest.mark.complete("ecryptfs-migrate-home ")
    def test_(self, completion):
        assert completion.list
