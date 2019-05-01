import pytest


class TestUname:
    @pytest.mark.complete(
        "uname --",
        xfail=(
            "! uname --help &>/dev/null || "
            "! uname --help 2>&1 | command grep -qF -- --help"
        ),
    )
    def test_1(self, completion):
        assert completion
