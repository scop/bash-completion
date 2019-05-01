import pytest


class TestGrep:
    @pytest.mark.complete(
        "grep --",
        xfail=(
            "! grep --help &>/dev/null || "
            "! grep --help 2>&1 | command grep -qF -- --help"
        ),
    )
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("grep --no-complete-dir f", cwd="shared/default")
    def test_2(self, completion):
        """
        Test --no-*dir isn't restricted to dirs only.

        Not really a grep option, but tests _longopt.
        """
        assert completion == "foo foo.d/".split()
