import pytest


class TestTac:
    @pytest.mark.complete(
        "tac --",
        xfail=(
            "! tac --help &>/dev/null || "
            "! tac --help 2>&1 | command grep -qF -- --help"
        ),
    )
    def test_1(self, completion):
        assert completion
