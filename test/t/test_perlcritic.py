import pytest


class TestPerlcritic:
    @pytest.mark.complete("perlcritic ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("perlcritic --", require_cmd=True)
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete("perlcritic --theme ", require_cmd=True)
    def test_3(self, completion):
        assert completion
