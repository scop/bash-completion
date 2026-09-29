import pytest


@pytest.mark.bashcomp(
    pre_cmds=("unalias -a", "alias foo=bar", "alias bar='foo foo'"),
    post_cmds=("unalias -a",),
)
class TestAlias:
    @pytest.mark.complete("alias ")
    def test_1(self, completion):
        assert completion == "bar foo".split()

    @pytest.mark.xfail  # TODO: Would like this completion to work
    @pytest.mark.complete("alias foo=")
    def test_2(self, completion):
        assert completion == "foo='bar'"
        assert not completion.endswith(" ")

    @pytest.mark.complete("alias ", trail="foo")
    def test_alias_at_point(self, completion):
        assert completion == "bar foo".split()

    @pytest.mark.complete("alias -")
    def test_options(self, completion):
        assert completion

    @pytest.mark.complete("alias -p ")
    def test_p(self, completion):
        assert not completion
