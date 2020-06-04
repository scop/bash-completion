import pytest


class TestCcache:
    @pytest.mark.complete("ccache -", require_cmd=True)
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("ccache --clea", require_cmd=True)
    def test_2(self, completion):
        assert all(x in completion for x in "--cleanup --clear".split())

    @pytest.mark.complete("ccache stt")
    def test_3(self, completion):
        assert completion == "y" or "stty" in completion

    @pytest.mark.complete("ccache --zero-stats stt")
    def test_4(self, completion):
        assert completion == "y" or "stty" in completion

    @pytest.mark.complete("ccache --hel", require_cmd=True)
    def test_5(self, completion):
        assert completion == "p" or "--help" in completion

    @pytest.mark.complete("ccache --zero-stats sh +")
    def test_6(self, completion):
        assert "+x" in completion
