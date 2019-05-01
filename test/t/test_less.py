import pytest


class TestLess:
    @pytest.mark.complete(
        "less --",
        xfail=(
            "! less --help &>/dev/null || "
            "! less --help 2>&1 | command grep -qF -- --help"
        ),
    )
    def test_1(self, completion):
        assert completion
