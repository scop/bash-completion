import pytest


class TestWc:
    @pytest.mark.complete(
        "wc --",
        xfail=(
            "! wc --help &>/dev/null || "
            "! wc --help 2>&1 | command grep -qF -- --help"
        ),
    )
    def test_1(self, completion):
        assert completion
