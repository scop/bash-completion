import pytest


class TestSort:
    @pytest.mark.complete(
        "sort --",
        require_cmd=True,
        xfail=(
            "! sort --help &>/dev/null || "
            "! sort --help 2>&1 | command grep -qF -- --help"
        ),
    )
    def test_1(self, completion):
        assert completion
