import pytest


class TestNetstat:
    @pytest.mark.complete("netstat ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("netstat -", require_longopt=True)
    def test_options(self, completion):
        assert completion
