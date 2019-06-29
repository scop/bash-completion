import pytest


@pytest.mark.bashcomp(pre_cmds=("PKG_DBDIR=$PWD/pkgtools/db",))
class TestPortupgrade:
    @pytest.mark.complete("portupgrade ")
    def test_1(self, completion):
        assert completion == "a b-c-d".split()
