import pytest


class TestBsdtar:
    @pytest.mark.complete("bsdtar xf bsdtar/")
    def test_readable_archives(self, completion):
        assert completion == "test.pax test.rar".split()

    @pytest.mark.complete("bsdtar uf bsdtar/")
    def test_writable_archives(self, completion):
        assert completion == "test.pax test.shar".split()
