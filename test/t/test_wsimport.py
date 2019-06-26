import pytest


class TestWsimport:
    @pytest.mark.complete("wsimport ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete(
        "wsimport -",
        require_cmd=True,
        xfail=(
            "! (wsimport -help 2>&1 || :) | "
            "command grep -q -- '[[:space:]]-'"
        ),
    )
    def test_2(self, completion):
        assert completion
