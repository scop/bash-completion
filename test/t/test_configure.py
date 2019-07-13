import pytest


@pytest.mark.bashcomp(
    pre_cmds=(
        # Make sure our own ./configure is in PATH
        "PATH=$PWD/../..:$PATH",
    )
)
class TestConfigure:
    @pytest.mark.complete("configure --", require_cmd=True)
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("configure --prefix ")
    def test_2(self, completion):
        assert completion
