import pytest


class TestTr:
    @pytest.mark.complete(
        "tr --",
        xfail=(
            "! tr --help &>/dev/null || "
            "! tr --help 2>&1 | command grep -qF -- --help"
        ),
    )
    def test_1(self, completion):
        assert completion
