import os

import pytest


@pytest.mark.bashcomp(ignore_env=r"^[+-]MANPATH=")
class TestMan:

    manpath = "$PWD/man"
    assumed_present = "man"

    @pytest.mark.complete("man bash-completion-testcas",
                          env=dict(MANPATH=manpath))
    def test_1(self, completion):
        assert completion.list == ["bash-completion-testcase"]

    @pytest.mark.complete("man man1/f", cwd="man", env=dict(MANPATH=manpath))
    def test_2(self, completion):
        assert completion.list == ["man1/foo.1"]

    @pytest.mark.complete("man man/", cwd="man", env=dict(MANPATH=manpath))
    def test_3(self, completion):
        assert completion.list == ["man/quux.8"]

    @pytest.mark.xfail(bool(os.environ.get("CI")) and
                       os.environ.get("DIST") == "centos6",
                       reason="TODO: Fails in CentOS for some reason, unknown "
                       "how to trigger same behavior as tests show (is "
                       "different and correct when tried manually, but here "
                       "at least in CI completes things it should not with "
                       "this MANPATH setting)")
    @pytest.mark.complete("man %s" % assumed_present, cwd="shared/empty_dir",
                          env=dict(MANPATH=manpath))
    def test_4(self, completion):
        """
        Assumed present should not be completed complete when there's no
        leading/trailing colon in $MANPATH.
        """
        assert not completion.list

    @pytest.mark.complete("man %s" % assumed_present,
                          cwd="shared/empty_dir",
                          env=dict(MANPATH="%s:" % manpath))
    def test_5(self, completion):
        """Trailing colon appends system man path."""
        assert completion.list

    @pytest.mark.complete(
        "man bash-completion-testcas", env=dict(MANPATH="%s:" % manpath))
    def test_6(self, completion):
        assert completion.list == ["bash-completion-testcase"]

    @pytest.mark.complete("man %s" % assumed_present,
                          cwd="shared/empty_dir",
                          env=dict(MANPATH=":%s" % manpath))
    def test_7(self, completion):
        """Leading colon prepends system man path."""
        assert completion.list

    @pytest.mark.complete(
        "man bash-completion-testcas", env=dict(MANPATH=":%s" % manpath))
    def test_8(self, completion):
        assert completion.list == ["bash-completion-testcase"]
