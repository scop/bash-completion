import pytest


class TestBc:
    @pytest.mark.complete(
        "bc --",
        xfail=(
            "! bc --help &>/dev/null || "
            "! bc --help 2>&1 | command grep -qF -- --help"
        ),
    )
    def test_1(self, completion):
        assert completion
