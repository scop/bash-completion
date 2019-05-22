import pytest


class TestEnv:
    @pytest.mark.complete(
        "env --",
        xfail=(
            "! env --help &>/dev/null || "
            "! env --help 2>&1 | command grep -qF -- --help"
        ),
    )
    def test_1(self, completion):
        assert completion
