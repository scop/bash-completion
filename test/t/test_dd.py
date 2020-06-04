import pytest


class TestDd:
    @pytest.mark.complete(
        "dd --",
        xfail=(
            "! dd --help &>/dev/null || "
            "! dd --help 2>&1 | command grep -qF -- --help"
        ),
    )
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("dd bs")
    def test_2(self, completion):
        assert completion == "="
