import pytest


class TestGpgv:
    @pytest.mark.complete("gpgv ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("gpgv -", require_cmd=True)
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete("gpgv foo.sig foo ")
    def test_3(self, completion):
        assert not completion
