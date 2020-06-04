import pytest


class TestFeh:
    @pytest.mark.complete("feh ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete(
        "feh --lis",
        xfail="feh --help 2>&1 | command grep -qF 'man feh'",
        require_cmd=True,
    )
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete("feh -S pix")
    def test_3(self, completion):
        assert completion == "els"

    @pytest.mark.complete("feh --zoom ma")
    def test_4(self, completion):
        assert completion == "x"

    @pytest.mark.complete("feh -g 640")
    def test_5(self, completion):
        assert completion == "0 1 2 3 4 5 6 7 8 9 x".split()

    @pytest.mark.complete("feh -g 640x48")
    def test_6(self, completion):
        assert completion == "0 1 2 3 4 5 6 7 8 9".split()
