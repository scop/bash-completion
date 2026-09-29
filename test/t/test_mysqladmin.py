import pytest


class TestMysqladmin:
    @pytest.mark.complete("mysqladmin -", require_cmd=True)
    def test_1(self, completion):
        assert completion
