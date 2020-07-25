import pytest

from conftest import assert_bash_exec


@pytest.mark.bashcomp(ignore_env=r"^\+ANT_ARGS=")
class TestAnt:
    @pytest.mark.complete("ant -", require_cmd=True)
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("ant ", cwd="ant")
    def test_2(self, completion):
        assert completion == "bashcomp clean init realclean".split()

    @pytest.mark.complete("ant -f build-with-import.xml ", cwd="ant")
    def test_3(self, completion):
        assert completion == "build-with-import imported-build".split()

    @pytest.mark.complete(
        "ant ", cwd="ant", env=dict(ANT_ARGS="'-f named-build.xml'")
    )
    def test_4(self, bash, completion):
        output = assert_bash_exec(bash, "complete -p ant", want_output=True)
        if "complete-ant-cmd.pl" in output:
            # Some versions of complete-ant-cmd.pl don't treat ANT_ARGS right;
            # in those cases we get the correct completion produced by _ant
            # plus whatever complete-ant-cmd.pl was able to get from build.xml
            assert "named-build" in completion
        else:
            assert completion == "named-build"

    @pytest.mark.complete("ant -l ")
    def test_5(self, completion):
        assert completion
