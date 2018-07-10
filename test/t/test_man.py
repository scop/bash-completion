import pytest


@pytest.mark.bashcomp(
    pre_cmds=(
        "export MANPATH=$PWD/man",
    ),
)
class TestMan(object):

    @pytest.mark.complete("man bash-completion-testcas")
    def test_1(self, completion):
        assert completion.list == ["bash-completion-testcase"]

    @pytest.mark.complete("man man1/f", cwd="man")
    def test_2(self, completion):
        assert completion.list == ["man1/foo.1"]

    @pytest.mark.complete("man man/", cwd="man")
    def test_3(self, completion):
        assert completion.list == ["man/quux.8"]
