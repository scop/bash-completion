import pytest


class TestDir:
    @pytest.mark.complete("dir ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("dir -", require_cmd=True)
    def test_options(self, completion):
        assert completion
