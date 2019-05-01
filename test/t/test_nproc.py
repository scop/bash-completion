import pytest


class TestNproc:
    @pytest.mark.complete("nproc ")
    def test_1(self, completion):
        assert not completion

    @pytest.mark.complete(
        "nproc --",
        xfail=(
            "! nproc --help &>/dev/null || "
            "! nproc --help 2>&1 | command grep -qF -- --help"
        ),
    )
    def test_2(self, completion):
        assert completion
