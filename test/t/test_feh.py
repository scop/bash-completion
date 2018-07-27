import pytest


class TestFeh:

    @pytest.mark.complete("feh ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("feh --lis",
                          skipif="feh --help 2>&1 | grep -qF 'man feh'")
    def test_2(self, completion):
        assert completion.list

    @pytest.mark.complete("feh -S pix")
    def test_3(self, completion):
        assert completion.list == ["pixels"]

    @pytest.mark.complete("feh --zoom ma")
    def test_4(self, completion):
        assert completion.list == ["max"]

    @pytest.mark.complete("feh -g 640")
    def test_5(self, completion):
        assert completion.list == "0 1 2 3 4 5 6 7 8 9 x".split()

    @pytest.mark.complete("feh -g 640x48")
    def test_6(self, completion):
        assert completion.list == "0 1 2 3 4 5 6 7 8 9".split()
