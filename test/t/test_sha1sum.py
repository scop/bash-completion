import pytest


class TestSha1sum:
    @pytest.mark.complete(
        "sha1sum --",
        xfail=(
            "! sha1sum --help &>/dev/null || "
            "! sha1sum --help 2>&1 | command grep -qF -- --help"
        ),
    )
    def test_1(self, completion):
        assert completion
