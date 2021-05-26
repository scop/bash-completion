import os

import pytest

from conftest import assert_bash_exec, assert_complete, bash_env_saved


@pytest.mark.bashcomp(cmd=None, temp_cwd=True)
class TestUnitQuoteReadline:
    def test_exec(self, bash):
        assert_bash_exec(bash, "quote_readline '' >/dev/null")

    def test_env_non_pollution(self, bash):
        """Test environment non-pollution, detected at teardown."""
        assert_bash_exec(
            bash, "foo() { quote_readline meh >/dev/null; }; foo; unset foo"
        )

    def test_github_issue_189_1(self, bash):
        """Test error messages on a certain command line

        Reported at https://github.com/scop/bash-completion/issues/189

        Syntax error messages should not be shown by completion on the
        following line:

          $ ls -- '${[TAB]
          $ rm -- '${[TAB]

        """
        assert_bash_exec(bash, "quote_readline $'\\'${' >/dev/null")

    def test_github_issue_492_1(self, bash):
        """Test unintended code execution on a certain command line

        Reported at https://github.com/scop/bash-completion/pull/492

        Arbitrary commands could be unintendedly executed by
        _quote_readline_by_ref.  In the following example, the command
        "touch 1.txt" would be unintendedly created before the fix.  The file
        "1.txt" should not be created by completion on the following line:

          $ echo '$(touch file.txt)[TAB]

        """
        assert_bash_exec(
            bash, "quote_readline $'\\'$(touch 1.txt)' >/dev/null"
        )
        assert not os.path.exists("./1.txt")

    def test_github_issue_492_2(self, bash):
        """Test the file clear by unintended redirection on a certain command line

        Reported at https://github.com/scop/bash-completion/pull/492

        The file "1.0" should not be created by completion on the following
        line:

          $ awk '$1 > 1.0[TAB]

        """
        assert_bash_exec(bash, "quote_readline $'\\'$1 > 1.0' >/dev/null")
        assert not os.path.exists("./1.0")

    def test_github_issue_492_3(self, bash):
        """Test code execution through unintended pathname expansions

        When there is a file named "quote=$(COMMAND)" (for _filedir) or
        "ret=$(COMMAND)" (for quote_readline), the completion of the word '$*
        results in the execution of COMMAND.

          $ echo '$*[TAB]

        """
        os.mkdir("./ret=$(echo injected >&2)")
        assert_bash_exec(bash, "quote_readline $'\\'$*' >/dev/null")

    def test_github_issue_492_4(self, bash):
        """Test error messages through unintended pathname expansions

        When "shopt -s failglob" is set by the user, the completion of the word
        containing glob character and special characters (e.g. TAB) results in
        the failure of pathname expansions.

          $ shopt -s failglob
          $ echo a\\	b*[TAB]

        """
        with bash_env_saved(bash) as bash_env:
            bash_env.shopt("failglob", True)
            assert_bash_exec(bash, "quote_readline $'a\\\\\\tb*' >/dev/null")

    def test_github_issue_526_1(self, bash):
        r"""Regression tests for unprocessed escape sequences after quotes

        Ref [1] https://github.com/scop/bash-completion/pull/492#discussion_r637213822
        Ref [2] https://github.com/scop/bash-completion/pull/526

        The escape sequences in the local variable of "value" in
        "_quote_readline_by_ref" needs to be unescaped by passing it to printf
        as the format string.  This causes a problem in the following case
        [where the spaces after "alpha\" is a TAB character inserted in the
        command string by "C-v TAB"]:

          $ echo alpha\   b[TAB]

        """
        os.mkdir("./alpha\tbeta")
        assert (
            assert_complete(
                # Remark on "rendered_cmd": Bash aligns the last character 'b'
                # in the rendered cmd to an "8 x n" boundary using spaces.
                # Here, the command string is assumed to start from column 2
                # because the width of PS1 (conftest.PS1 = '/@') is 2,
                bash,
                "echo alpha\\\026\tb",
                rendered_cmd="echo alpha\\   b",
            )
            == "eta/"
        )
