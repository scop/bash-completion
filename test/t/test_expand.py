import pytest


class TestExpand:
    @pytest.mark.complete(
        "expand --",
        require_cmd=True,
        xfail=(
            "! expand --help &>/dev/null || "
            "! expand --help 2>&1 | command grep -qF -- --help"
        ),
    )
    def test_1(self, completion):
        assert completion
