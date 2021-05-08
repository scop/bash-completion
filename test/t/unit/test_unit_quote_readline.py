import pytest
import os

from conftest import assert_bash_exec


@pytest.mark.bashcomp(cmd=None)
class TestUnitQuoteReadline:
    def test_exec(self, bash):
        assert_bash_exec(bash, "quote_readline '' >/dev/null")

    def test_env_non_pollution(self, bash):
        """Test environment non-pollution, detected at teardown."""
        assert_bash_exec(
            bash, "foo() { quote_readline meh >/dev/null; }; foo; unset foo"
        )

    # https://github.com/scop/bash-completion/issues/189
    # Syntax error messages should not be shown by completion on the following
    # line:
    #
    #   $ ls -- '${[TAB]
    #   $ rm -- '${[TAB]
    #
    def test_github_issue_189_1(self, bash):
        assert_bash_exec(bash, "quote_readline $'\\'${' >/dev/null")

    # https://github.com/scop/bash-completion/pull/492
    # Arbitrary commands could be unintendedly executed by 
    # _quote_readline_by_ref.  In the following example, the command 
    # "touch 1.txt" would be unintendedly created before the fix.  The file
    # "1.txt" should not be created by completion on the following line:
    #
    #   $ echo '$(touch file.txt)[TAB]
    #
    def test_github_issue_492_1(self, bash):
        if os.path.exists("1.txt"):
            os.remove("1.txt")
        assert_bash_exec(bash, "quote_readline $'\\'$(touch 1.txt)' >/dev/null")
        if os.path.exists("1.txt"):
            os.remove("1.txt")
            assert False

    # https://github.com/scop/bash-completion/pull/492
    # The file "1.0" should not be created by completion on the following line:
    #
    #   $ awk '$1 > 1.0[TAB]
    #
    def test_github_issue_492_2(self, bash):
        if os.path.exists("1.0"):
            os.remove("1.0")
        assert_bash_exec(bash, "quote_readline $'\\'$1 > 1.0' >/dev/null")
        if os.path.exists("1.0"):
            os.remove("1.0")
            assert False

    # When there is a file named "quote=$(COMMAND)" (for _filedir) or
    # "ret=$(COMMAND)" (for quote_readline), the completion of the word '$*
    # results in the execution of COMMAND.
    #
    #   $ echo '$*[TAB]
    #
    def test_github_issue_492_3(self, bash):
        tmpfile = "ret=$(echo injected >&2)"
        with open(tmpfile, 'a'):
            os.utime(tmpfile, None)
        assert_bash_exec(bash, "quote_readline $'\\'$*' >/dev/null")
        if os.path.exists(tmpfile):
            os.remove(tmpfile)

    # When "shopt -s failglob" is set by the user, the completion of the word
    # containing glob character and special characters (e.g. TAB) results in
    # the failure of pathname expansions.
    #
    #   $ shopt -s failglob
    #   $ echo a\	b*[TAB]
    #
    def test_github_issue_492_4(self, bash):
        assert_bash_exec(bash, "(shopt -s failglob;quote_readline $'a\\\\\\tb*' >/dev/null)")
