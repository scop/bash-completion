import pytest


class TestLd:
    @pytest.mark.complete("ld ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("ld -", require_cmd=True)
    def test_options(self, completion):
        assert completion
