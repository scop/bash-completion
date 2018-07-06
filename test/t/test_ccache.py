import pytest


class Test(object):

    @pytest.mark.complete("ccache -")
    def test_(self, completion):
        assert completion.list

    @pytest.mark.complete("ccache --clea")
    def test_clea(self, completion):
        assert "--cleanup" in completion.list and "--clear" in completion.list

    @pytest.mark.complete("ccache stt")
    def test_command(self, completion):
        assert "stty" in completion.list

    @pytest.mark.complete("ccache --zero-stats stt")
    def test_command_after_flag(self, completion):
        assert "stty" in completion.list

    @pytest.mark.complete("ccache --hel")
    def test_hel(self, completion):
        assert "--help" in completion.list

    @pytest.mark.complete("ccache --zero-stats ls --hel")
    def test_command_flags(self, completion):
        assert "--help" in completion.list
