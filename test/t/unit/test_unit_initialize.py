import pytest

from conftest import TestUnitBase, assert_bash_exec, assert_complete


@pytest.mark.bashcomp(
    cmd=None,
    ignore_env=r"^[+-](COMP(_(WORDS|CWORD|LINE|POINT)|REPLY)|"
    r"cur|prev|cword|words)=|^\+declare -f _cmd1$",
)
class TestUnitInitCompletion(TestUnitBase):
    def test_1(self, bash):
        """Test environment non-pollution, detected at teardown."""
        assert_bash_exec(
            bash,
            "foo() { "
            "local cur prev words cword comp_args "
            "COMP_WORDS=() COMP_CWORD=0 COMP_LINE= COMP_POINT=0; "
            "_comp_initialize; }; "
            "foo; unset -f foo",
        )

    def test_2(self, bash):
        output = self._test_unit(
            "_comp_initialize %s; echo $cur,${prev-}", bash, "(a)", 0, "a", 0
        )
        assert output == ","

    @pytest.mark.parametrize("redirect", "> >> 2> < &>".split())
    def test_redirect(self, bash, redirect):
        completion = assert_complete(
            bash, "%s " % redirect, cwd="shared/default"
        )
        assert all(x in completion for x in "foo bar".split())

    @pytest.fixture(scope="class")
    def cmd1_empty_completion_setup(self, bash):
        assert_bash_exec(
            bash,
            '_cmd1() { local cur prev words cword comp_args; _comp_initialize -- "$@"; } && '
            "complete -F _cmd1 cmd1",
        )

    @pytest.mark.parametrize("redirect", "> >> 2> {fd1}> < &> &>> >|".split())
    def test_redirect_2(self, bash, cmd1_empty_completion_setup, redirect):
        # Note: Bash 4.3 and below cannot properly extract the redirection ">|"
        if redirect == ">|":
            skipif = "((BASH_VERSINFO[0] * 100 + BASH_VERSINFO[1] < 404))"
            try:
                assert_bash_exec(bash, skipif, want_output=None)
            except AssertionError:
                pass
            else:
                pytest.skip(skipif)

        completion = assert_complete(
            bash, "cmd1 %s f" % redirect, cwd="shared/default"
        )
        assert "foo" in completion

    @pytest.mark.parametrize("redirect", "> >> 2> < &>".split())
    def test_redirect_3(self, bash, redirect):
        completion = assert_complete(
            bash, "cmd1 %sf" % redirect, cwd="shared/default"
        )
        assert "foo" in completion
