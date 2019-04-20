import pytest


class TestXmlwf:
    @pytest.mark.complete("xmlwf ")
    def test_1(self, completion):
        assert completion
