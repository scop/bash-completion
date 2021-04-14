import pytest


class TestPdftoppm:
    @pytest.mark.complete("pdftoppm ")
    def test_files(self, completion):
        assert completion

    @pytest.mark.complete("pdftoppm -", require_cmd=True)
    def test_options(self, completion):
        assert completion
