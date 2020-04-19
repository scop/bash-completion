import pytest

from conftest import complete_at_point


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

    def test_alias_at_point(self, bash):
        assert complete_at_point(
            bash=bash, cmd="alias ", trail="foo", expected=r"bar\s+foo\s*?"
        )
