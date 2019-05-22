import pytest


class TestXmlwf:
    @pytest.mark.complete("xmlwf ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("xmlwf -")
    def test_2(self, completion):
        assert completion
