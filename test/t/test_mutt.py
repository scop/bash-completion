import pytest

from conftest import assert_bash_exec


@pytest.mark.bashcomp(pre_cmds=("HOME=$PWD/mutt",))
class TestMutt:
    @pytest.mark.complete("mutt -")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("mutt -F muttrc -f =", require_cmd=True, cwd="mutt")
    def test_2(self, completion):
        assert completion == "bar/ foo/ muttrc".split()

    @pytest.mark.complete("mutt -F muttrc -A ", cwd="mutt")
    def test_3(self, completion):
        assert completion == "a1 a2".split()

    def test_4(self, bash):
        got = (
            assert_bash_exec(
                bash,
                '_muttconffiles "$HOME/muttrc" "$HOME/muttrc"',
                want_output=True,
            )
            .strip()
            .split()
        )
        assert got == [
            "%s/mutt/%s" % (bash.cwd, x)
            for x in ("muttrc", "bar/muttrc_b", "foo/muttrc_f")
        ]
