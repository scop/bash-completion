import pytest


class TestCcache(object):

    @pytest.mark.complete("ccache -")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("ccache --clea")
    def test_2(self, completion):
        assert "--cleanup" in completion.list and "--clear" in completion.list

    @pytest.mark.complete("ccache stt")
    def test_3(self, completion):
        assert "stty" in completion.list

    @pytest.mark.complete("ccache --zero-stats stt")
    def test_4(self, completion):
        assert "stty" in completion.list

    @pytest.mark.complete("ccache --hel")
    def test_5(self, completion):
        assert "--help" in completion.list

    @pytest.mark.complete("ccache --zero-stats ls --hel")
    def test_6(self, completion):
        assert "--help" in completion.list
