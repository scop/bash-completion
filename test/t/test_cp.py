import pytest


class TestCp:
    @pytest.mark.complete("cp ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("cp -", require_cmd=True)
    def test_options(self, completion):
        assert completion
