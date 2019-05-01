import pytest


class TestUnexpand:
    @pytest.mark.complete(
        "unexpand --",
        xfail=(
            "! unexpand --help &>/dev/null || "
            "! unexpand --help 2>&1 | command grep -qF -- --help"
        ),
    )
    def test_1(self, completion):
        assert completion
