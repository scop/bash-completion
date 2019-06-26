import pytest


class TestTail:
    @pytest.mark.complete(
        "tail --",
        require_cmd=True,
        xfail=(
            "! tail --help &>/dev/null || "
            "! tail --help 2>&1 | command grep -qF -- --help"
        ),
    )
    def test_1(self, completion):
        assert completion
