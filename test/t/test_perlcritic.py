import pytest


class TestPerlcritic:

    @pytest.mark.complete("perlcritic ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("perlcritic --")
    def test_2(self, completion):
        assert completion.list

    @pytest.mark.complete("perlcritic --theme ")
    def test_3(self, completion):
        assert completion.list
