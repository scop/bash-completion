import pytest


class TestGzip:
    @pytest.mark.complete("gzip ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("gzip ~")
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete("gzip -", require_cmd=True)
    def test_3(self, completion):
        assert completion
