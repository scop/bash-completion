import pytest


class TestRm:
    @pytest.mark.complete("rm ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("rm -", require_cmd=True)
    def test_options(self, completion):
        assert completion
