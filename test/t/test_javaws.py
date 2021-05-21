import pytest


class TestJavaws:
    @pytest.mark.complete("javaws ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete(
        "javaws -",
        require_cmd=True,
        xfail=(
            "! (javaws -help 2>&1 || :) | " "command grep -q -- '[[:space:]]-'"
        ),
    )
    def test_2(self, completion):
        assert completion
