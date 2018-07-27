import pytest


@pytest.mark.bashcomp(
    pre_cmds=(
        "unalias -a",
        "alias foo=bar",
        "alias bar='foo foo'",
    ),
    post_cmds=(
        "unalias -a",
    ),
)
class TestAlias:

    @pytest.mark.complete("alias ")
    def test_1(self, completion):
        assert completion.list == "bar foo".split()

    @pytest.mark.xfail  # TODO: Would like this completion to work
    @pytest.mark.complete("alias foo=")
    def test_2(self, completion):
        assert completion.list == ["foo='bar'"]
        assert not completion.line.endswith(" ")
