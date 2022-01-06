import pytest

from conftest import (
    assert_bash_exec,
    assert_complete,
    is_bash_type,
    prepare_fixture_dir,
)


@pytest.mark.bashcomp(
    ignore_env=r"^[+-]((BASHOPTS|MANPATH|manpath)=|shopt -. failglob)"
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
        tmpdir, _, _ = prepare_fixture_dir(
            request,
            files=["man/man3/Bash::Completion.3pm.gz"],
            dirs=["man", "man/man3"],
        )
        return tmpdir

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
        shopt=dict(failglob=True),
    )
    def test_9(self, bash, completion):
        assert self.assumed_present in completion

    def test_10(self, request, bash, colonpath):
        if not is_bash_type(bash, "man"):
            pytest.skip("Command not found")
        completion = assert_complete(
            bash,
            "man Bash::C",
            env=dict(MANPATH="%s:%s/man" % (TestMan.manpath, colonpath)),
        )
        assert completion == "ompletion"

    @pytest.mark.complete("man -", require_cmd=True)
    def test_11(self, completion):
        assert completion

    @pytest.mark.complete("man -S 1", require_cmd=True)
    def test_delimited_first(self, completion):
        # just appends space
        assert not completion
        assert completion.endswith(" ")

    @pytest.mark.complete("man -S 1:", require_cmd=True)
    def test_delimited_after_delimiter(self, completion):
        assert completion
        assert "1" not in completion

    @pytest.mark.complete("man -S 1:2", require_cmd=True)
    def test_delimited_later(self, completion):
        # just appends space
        assert not completion
        assert completion.endswith(" ")

    @pytest.mark.complete("man -S 1:1", require_cmd=True)
    def test_delimited_deduplication(self, completion):
        # no completion, no space appended
        assert not completion
        assert not completion.endswith(" ")

    @pytest.mark.complete(
        "man bash-completion-zstd-testcas",
        env=dict(MANPATH=manpath),
        require_cmd=True,
    )
    def test_zstd_arbitrary_sectsuffix(self, completion):
        assert completion == "e"

    @pytest.mark.complete(
        "man bash-completion-testcas",
        env=dict(MANPATH="'$(echo malicious code >/dev/tty)'"),
    )
    def test_manpath_code_injection(self, completion):
        # no completion, no space appended
        assert not completion
