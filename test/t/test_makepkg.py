import pytest


@pytest.mark.bashcomp(
    xfail="! makepkg --help 2>&1 | command grep -qiF slackware"
)
class TestMakepkg:
    @pytest.mark.complete("makepkg ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("makepkg --")
    def test_2(self, completion):
        assert all(
            x in completion for x in "--chown --linkadd --prepend".split()
        )
