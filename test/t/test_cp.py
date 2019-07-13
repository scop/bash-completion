import pytest


class TestCp:
    @pytest.mark.complete("cp ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("cp -", require_longopt=True)
    def test_options(self, completion):
        assert completion
