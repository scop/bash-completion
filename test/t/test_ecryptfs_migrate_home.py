import pytest


class TestEcryptfsMigrateHome(object):

    @pytest.mark.complete("ecryptfs-migrate-home ")
    def test_1(self, completion):
        assert completion.list
