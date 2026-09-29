import pytest

from conftest import assert_bash_exec


@pytest.mark.bashcomp(
    ignore_env=r"^\+ANT_ARGS=",
    temp_cwd=True,
    pre_cmds=('cp "$SRCDIRABS"/fixtures/ant/*.xml .',),
)
class TestAnt:
    @pytest.fixture(scope="class")
    def has_complete_ant_cmd_pl(self, bash):
        output = assert_bash_exec(bash, "complete -p ant", want_output=True)
        return "complete-ant-cmd.pl" in output

    @pytest.mark.complete("ant -", require_cmd=True)
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("ant ")
    def test_2(self, completion):
        assert completion == "bashcomp clean init realclean".split()

    @pytest.mark.complete("ant -f build-with-import.xml ")
    def test_3(self, completion, has_complete_ant_cmd_pl):
        if has_complete_ant_cmd_pl:
            # Some versions of complete-ant-cmd.pl add "import-project-name."
            # prefix to imported targets, just check that the ones we add
            # are there.
            assert all(
                x in completion
                for x in "build-with-import imported-build".split()
            )
        else:
            assert completion == "build-with-import imported-build".split()

    @pytest.mark.complete("ant ", env=dict(ANT_ARGS="'-f named-build.xml'"))
    def test_4(self, bash, completion, has_complete_ant_cmd_pl):
        if has_complete_ant_cmd_pl:
            # Some versions of complete-ant-cmd.pl don't treat ANT_ARGS right;
            # in those cases we get the correct completion produced by us
            # plus whatever complete-ant-cmd.pl was able to get from build.xml
            assert "named-build" in completion
        else:
            assert completion == "named-build"

    @pytest.mark.complete("ant -l ")
    def test_5(self, completion):
        assert completion
