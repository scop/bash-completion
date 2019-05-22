import pytest


class TestFold:
    @pytest.mark.complete(
        "fold --",
        xfail=(
            "! fold --help &>/dev/null || "
            "! fold --help 2>&1 | command grep -qF -- --help"
        ),
    )
    def test_1(self, completion):
        assert completion
