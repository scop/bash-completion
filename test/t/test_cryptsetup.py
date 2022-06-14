import pytest


class TestCryptsetup:
    @pytest.mark.complete("cryptsetup ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("cryptsetup -", require_cmd=True)
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete("cryptsetup luksE", require_cmd=True)
    def test_github_issue758(self, completion):
        assert completion == "rase"
