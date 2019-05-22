import pytest


class TestTouch:
    @pytest.mark.complete(
        "touch --",
        xfail=(
            "! touch --help &>/dev/null || "
            "! touch --help 2>&1 | command grep -qF -- --help"
        ),
    )
    def test_1(self, completion):
        assert completion
