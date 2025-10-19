import pytest


class TestComm:
    @pytest.mark.complete("comm ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("comm -", require_longopt=True)
    def test_options(self, completion):
        assert completion
