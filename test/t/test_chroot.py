import pytest


class TestChroot:
    @pytest.mark.complete("chroot ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("/bin/chroot shared/default/")
    def test_2(self, completion):
        """Should complete dirs only, also when invoked using full path."""
        assert completion == ["bar bar.d/", "foo.d/"]

    @pytest.mark.complete("chroot -", require_longopt=True)
    def test_options(self, completion):
        assert completion
