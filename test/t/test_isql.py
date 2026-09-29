import pytest


@pytest.mark.bashcomp(pre_cmds=("ODBCINI=isql/odbc.ini",))
class TestIsql:
    @pytest.mark.complete("isql ")
    def test_1(self, completion):
        assert completion
