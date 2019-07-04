import pytest


class TestPtx:
    @pytest.mark.complete("ptx ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("ptx -", require_cmd=True)
    def test_options(self, completion):
        assert completion
