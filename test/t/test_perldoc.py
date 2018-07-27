import pytest


@pytest.mark.bashcomp(
    pre_cmds=(
        "export PERL5LIB=$PWD/perldoc",
    ),
)
class TestPerldoc:

    @pytest.mark.complete("perldoc File::")
    def test_1(self, completion):
        assert "Path" in completion.list  # Assume File::Path always installed
        assert "fixtures/" not in completion.list  # Our fixtures/ dir
        assert not [x for x in completion.list if "File::File::" in x]

    @pytest.mark.complete("perldoc -")
    def test_2(self, completion):
        assert completion.list

    @pytest.mark.complete("perldoc BashCompletion")
    def test_3(self, completion):
        assert completion.list == ["BashCompletionDoc", "BashCompletionModule"]
