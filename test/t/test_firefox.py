import pytest


class TestFirefox:
    @pytest.mark.complete("firefox ")
    def test_1(self, completion):
        assert completion

    # --help test: running as root in GH actions container croaks:
    #     Running Firefox as root in a regular user's session is not supported.
    #     ($HOME is /github/home which is owned by uid 1001.)
    @pytest.mark.complete(
        "firefox -", require_cmd=True, xfail="! firefox --help &>/dev/null"
    )
    def test_2(self, completion):
        assert completion
        assert not completion.endswith(" ")
