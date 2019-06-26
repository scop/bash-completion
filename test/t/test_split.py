import pytest


class TestSplit:
    @pytest.mark.complete(
        "split --",
        require_cmd=True,
        xfail=(
            "! split --help &>/dev/null || "
            "! split --help 2>&1 | command grep -qF -- --help"
        ),
    )
    def test_1(self, completion):
        assert completion
