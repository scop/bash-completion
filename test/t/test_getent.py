import pytest


class TestGetent:
    @pytest.mark.complete("getent ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete(
        "getent -",
        require_cmd=True,
        xfail=(
            "! (getent --help 2>&1 || :) | "
            "command grep -q -- '[[:space:]]-'"
        ),
    )
    def test_2(self, completion):
        assert completion
