import pytest


class TestSeq:
    @pytest.mark.complete(
        "seq --",
        xfail=(
            "! seq --help &>/dev/null || "
            "! seq --help 2>&1 | command grep -qF -- --help"
        ),
    )
    def test_1(self, completion):
        assert completion
