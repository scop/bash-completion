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

    @pytest.mark.complete(
        "lrzip --",
        # require_longopt not applicable, useful --help may give nonzero exit
        require_cmd=True,
        xfail=("! { lrzip --help 2>&1 || :; } | command grep -qF -- --help"),
    )
    def test_longopt(self, completion):
        assert completion
