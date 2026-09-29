import pytest


class TestIrb:
    @pytest.mark.complete("irb ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("irb -", require_longopt=True)
    def test_options(self, completion):
        assert completion
