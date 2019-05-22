import os

import pytest

from conftest import assert_bash_exec, in_container


@pytest.mark.bashcomp(ignore_env=r"^[+-]MANPATH=")
class TestMan:

    manpath = "$PWD/man"
    assumed_present = "man"

    @pytest.fixture
    def colonpath(self, request, bash):
        try:
            assert_bash_exec(bash, "uname -s 2>&1 | grep -qiF cygwin")
        except AssertionError:
            pass
        else:
            pytest.skip("Cygwin doesn't like paths with colons")
            return
        assert_bash_exec(bash, "mkdir -p $TESTDIR/../tmp/man/man3")
        assert_bash_exec(
            bash, "touch $TESTDIR/../tmp/man/man3/Bash::Completion.3pm.gz"
        )
        request.addfinalizer(
            lambda: assert_bash_exec(bash, "rm -r $TESTDIR/../tmp/man")
        )

    @pytest.mark.complete(
        "man bash-completion-testcas", env=dict(MANPATH=manpath)
    )
    def test_1(self, completion):
        assert completion == "bash-completion-testcase"

    @pytest.mark.complete("man man1/f", cwd="man", env=dict(MANPATH=manpath))
    def test_2(self, completion):
        assert completion == "man1/foo.1"

    @pytest.mark.complete("man man/", cwd="man", env=dict(MANPATH=manpath))
    def test_3(self, completion):
        assert completion == "man/quux.8"

    @pytest.mark.xfail(
        in_container() and os.environ.get("DIST") == "centos6",
        reason="TODO: Fails in CentOS for some reason, unknown "
        "how to trigger same behavior as tests show (is "
        "different and correct when tried manually, but here "
        "at least in CI completes things it should not with "
        "this MANPATH setting)",
    )
    @pytest.mark.complete(
        "man %s" % assumed_present,
        cwd="shared/empty_dir",
        env=dict(MANPATH=manpath),
    )
    def test_4(self, completion):
        """
        Assumed present should not be completed complete when there's no
        leading/trailing colon in $MANPATH.
        """
        assert not completion

    @pytest.mark.complete(
        "man %s" % assumed_present,
        cwd="shared/empty_dir",
        env=dict(MANPATH="%s:" % manpath),
    )
    def test_5(self, completion):
        """Trailing colon appends system man path."""
        assert completion

    @pytest.mark.complete(
        "man bash-completion-testcas", env=dict(MANPATH="%s:" % manpath)
    )
    def test_6(self, completion):
        assert completion == "bash-completion-testcase"

    @pytest.mark.complete(
        "man %s" % assumed_present,
        cwd="shared/empty_dir",
        env=dict(MANPATH=":%s" % manpath),
    )
    def test_7(self, completion):
        """Leading colon prepends system man path."""
        assert completion

    @pytest.mark.complete(
        "man bash-completion-testcas", env=dict(MANPATH=":%s" % manpath)
    )
    def test_8(self, completion):
        assert completion == "bash-completion-testcase"

    @pytest.mark.complete(
        "man %s" % assumed_present,
        cwd="shared/empty_dir",
        pre_cmds=("shopt -s failglob",),
    )
    def test_9(self, bash, completion):
        assert self.assumed_present in completion
        assert_bash_exec(bash, "shopt -u failglob")

    @pytest.mark.complete(
        "man Bash::C", env=dict(MANPATH="%s:../tmp/man" % manpath)
    )
    def test_10(self, bash, colonpath, completion):
        assert completion == "Bash::Completion"

    @pytest.mark.complete("man -")
    def test_11(self, completion):
        assert completion
