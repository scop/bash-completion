import pytest


class TestPwdx:
    @pytest.mark.complete("pwdx ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete(
        "pwdx -",
        require_cmd=True,
        xfail=(
            "! (pwdx --help 2>&1 || :) | "
            "command grep -vF 'invalid process id: --help' | "
            "command grep -q -- '[[:space:]]-'"
        ),
    )
    def test_2(self, completion):
        assert completion
