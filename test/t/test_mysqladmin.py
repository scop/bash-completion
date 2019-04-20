import pytest


class TestMysqladmin:
    @pytest.mark.complete("mysqladmin -")
    def test_1(self, completion):
        assert completion
