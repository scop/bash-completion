import pytest


class TestAwk:
    @pytest.mark.complete("awk ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("awk -", require_longopt=True)
    def test_options(self, completion):
        assert completion
