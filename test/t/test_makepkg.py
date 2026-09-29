import pytest


@pytest.mark.bashcomp(
    ignore_env=r"^-declare -f _comp_cmd_makepkg__bootstrap$",
    xfail="! makepkg --help 2>&1 | command grep -qiF slackware",
)
class TestMakepkg:
    @pytest.mark.complete("makepkg ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("makepkg --", require_cmd=True)
    def test_2(self, completion):
        assert all(
            x in completion for x in "--chown --linkadd --prepend".split()
        )
