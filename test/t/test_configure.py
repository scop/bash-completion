import pytest


@pytest.mark.bashcomp(
    pre_cmds=(
        # Make sure our own ./configure is in PATH
        "PATH=$PWD/../..:$PATH",
    ),
)
class TestConfigure(object):

    @pytest.mark.complete("configure --")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("configure --prefix ")
    def test_2(self, completion):
        assert completion.list
