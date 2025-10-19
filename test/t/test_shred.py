import pytest


class TestShred:
    @pytest.mark.complete("shred ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("shred -", require_longopt=True)
    def test_options(self, completion):
        assert completion
