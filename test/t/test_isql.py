import pytest


@pytest.mark.pre_commands(
    "ODBCINI=isql/odbc.ini",
)
class TestIsql(object):

    @pytest.mark.complete("isql ")
    def test_1(self, completion):
        assert completion.list
