import pytest


@pytest.mark.bashcomp(cmd="chromium-browser")
class TestChromiumBrowser:
    @pytest.mark.complete("chromium-browser ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete(
        "chromium-browser -", xfail="! chromium-browser --help &>/dev/null"
    )
    def test_2(self, completion):
        assert completion
        assert not completion.endswith(" ")

    @pytest.mark.complete("chromium-browser --proxy-server=")
    def test_proxy_server_scheme(self, completion):
        assert completion
        assert not completion.endswith(" ")
        assert all(x.endswith("://") for x in completion)

    @pytest.mark.complete("chromium-browser --proxy-server=http://")
    def test_proxy_server_host(self, completion):
        assert completion
