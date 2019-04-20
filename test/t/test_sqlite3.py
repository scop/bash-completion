import pytest


class TestSqlite3:
    @pytest.mark.complete("sqlite3 ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("sqlite3 -")
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete("sqlite3 -scratch foo ")
    def test_3(self, completion):
        assert not completion
