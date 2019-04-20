import pytest


class TestImport:
    @pytest.mark.complete("import ")
    def test_1(self, completion):
        assert completion
