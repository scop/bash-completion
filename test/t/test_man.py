import pytest

from conftest import assert_bash_exec


@pytest.mark.bashcomp(
    ignore_env=r"^[+-]((BASHOPTS|MANPATH)=|shopt -. failglob)"
)
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
        "man bash-completion-testcas",
        env=dict(MANPATH=manpath),
        require_cmd=True,
    )
    def test_1(self, completion):
        assert completion == "e"

    @pytest.mark.complete("man man1/f", cwd="man", env=dict(MANPATH=manpath))
    def test_2(self, completion):
        assert completion == "oo.1"

    @pytest.mark.complete("man man/", cwd="man", env=dict(MANPATH=manpath))
    def test_3(self, completion):
        assert completion == "quux.8"

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
        require_cmd=True,
        cwd="shared/empty_dir",
        env=dict(MANPATH="%s:" % manpath),
    )
    def test_5(self, completion):
        """Trailing colon appends system man path."""
        assert completion

    @pytest.mark.complete(
        "man bash-completion-testcas",
        require_cmd=True,
        env=dict(MANPATH="%s:" % manpath),
    )
    def test_6(self, completion):
        assert completion == "e"

    @pytest.mark.complete(
        "man %s" % assumed_present,
        require_cmd=True,
        cwd="shared/empty_dir",
        env=dict(MANPATH=":%s" % manpath),
    )
    def test_7(self, completion):
        """Leading colon prepends system man path."""
        assert completion

    @pytest.mark.complete(
        "man bash-completion-testcas",
        require_cmd=True,
        env=dict(MANPATH=":%s" % manpath),
    )
    def test_8(self, completion):
        assert completion == "e"

    @pytest.mark.complete(
        "man %s" % assumed_present,
        require_cmd=True,
        cwd="shared/empty_dir",
        pre_cmds=("shopt -s failglob",),
    )
    def test_9(self, bash, completion):
        assert self.assumed_present in completion
        assert_bash_exec(bash, "shopt -u failglob")

    @pytest.mark.complete(
        "man Bash::C",
        require_cmd=True,
        env=dict(MANPATH="%s:../tmp/man" % manpath),
    )
    def test_10(self, bash, colonpath, completion):
        assert completion == "ompletion"

    @pytest.mark.complete("man -", require_cmd=True)
    def test_11(self, completion):
        assert completion
