import pytest


class TestDict:
    @pytest.mark.complete("dict -", require_cmd=True)
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("dict --database ", require_cmd=True)
    def test_database(self, completion):
        assert completion
