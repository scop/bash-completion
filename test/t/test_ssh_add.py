import pytest


@pytest.mark.bashcomp(cmd="ssh-add")
class TestSshAdd:
    @pytest.mark.complete("ssh-add ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete(
        "ssh-add -",
        require_cmd=True,
        xfail="ssh-add --help 2>&1 | "
        "command grep -qiF 'Could not open a connection'",
    )
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete(
        "ssh-add -",
        require_cmd=True,
        xfail="ssh-add --help 2>&1 | "
        "command grep -qiF 'Could not open a connection'",
        shopt=dict(failglob=True),
    )
    def test_2_failglob(self, completion):
        assert completion

    @pytest.mark.complete(
        "ssh-add -",
        require_cmd=True,
        xfail="ssh-add --help 2>&1 | "
        "command grep -qiF 'Could not open a connection'",
        shopt=dict(nullglob=True),
    )
    def test_2_nullglob(self, completion):
        assert completion
