import pytest


class TestSha256sum:
    @pytest.mark.complete("sha256sum --", require_longopt=True)
    def test_options(self, completion):
        assert completion

    @pytest.mark.complete("sha256sum ", cwd="sha256sum")
    def test_summing(self, completion):
        assert completion == "foo"

    @pytest.mark.complete("sha256sum -c ", cwd="sha256sum")
    def test_checking(self, completion):
        assert completion == "foo.sha256"
