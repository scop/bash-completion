import pytest


class TestLrzip:
    @pytest.mark.complete("lrzip ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("lrzip ~")
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete("lrzip -", require_cmd=True)
    def test_3(self, completion):
        assert completion
