import pytest


@pytest.mark.bashcomp(
    cmd="ecryptfs-migrate-home",
)
class TestEcryptfsMigrateHome:

    @pytest.mark.complete("ecryptfs-migrate-home ")
    def test_1(self, completion):
        assert completion.list
