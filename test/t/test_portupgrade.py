import pytest


@pytest.mark.bashcomp(pre_cmds=("PKG_DBDIR=$PWD/dbtools/db",))
class TestPortupgrade:
    @pytest.mark.complete("portupgrade ")
    def test_1(self, completion):
        assert completion == "a b-c-d".split()
        assert completion.endswith(" ")
