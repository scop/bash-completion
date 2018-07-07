import pytest


@pytest.mark.pre_commands(
    # Make sure our own ./configure is in PATH
    "PATH+=:$PWD/../..",
)
class TestConfigure(object):

    @pytest.mark.complete("configure --")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("configure --prefix ")
    def test_2(self, completion):
        assert completion.list
