import pytest


class TestConvert:
    @pytest.mark.complete("convert ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("convert -format ")
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete("convert -", require_cmd=True)
    def test_3(self, completion):
        assert completion
