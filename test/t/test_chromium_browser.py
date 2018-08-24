import pytest


@pytest.mark.bashcomp(
    cmd="chromium-browser",
)
class TestChromiumBrowser:

    @pytest.mark.complete("chromium-browser ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("chromium-browser -")
    def test_2(self, completion):
        assert completion.list
        assert not completion.line.endswith(" ")
