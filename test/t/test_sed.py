import pytest


class TestSed:
    @pytest.mark.complete(
        "sed --",
        xfail=(
            "! sed --help &>/dev/null || "
            "! sed --help 2>&1 | command grep -qF -- --help"
        ),
    )
    def test_1(self, completion):
        assert completion
