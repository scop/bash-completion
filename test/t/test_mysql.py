import pytest


class TestMysql:
    @pytest.mark.complete("mysql --")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("mysql --default-character-set=")
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete("mysql --non-existent-option=--")
    def test_3(self, completion):
        assert not completion
