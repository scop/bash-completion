import pytest


class TestXsltproc:
    @pytest.mark.complete("xsltproc ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("xsltproc -", require_cmd=True)
    def test_2(self, completion):
        assert completion
