import pytest


class TestXmllint:
    @pytest.mark.complete("xmllint ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("xmllint -")
    def test_2(self, completion):
        assert completion
