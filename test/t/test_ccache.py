import pytest


class TestCcache:
    @pytest.mark.complete("ccache -")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("ccache --clea")
    def test_2(self, completion):
        assert all(x in completion for x in "--cleanup --clear".split())

    @pytest.mark.complete("ccache stt")
    def test_3(self, completion):
        assert "stty" in completion

    @pytest.mark.complete("ccache --zero-stats stt")
    def test_4(self, completion):
        assert "stty" in completion

    @pytest.mark.complete("ccache --hel")
    def test_5(self, completion):
        assert "--help" in completion

    @pytest.mark.complete("ccache --zero-stats ls --hel")
    def test_6(self, completion):
        assert "--help" in completion
