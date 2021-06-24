import pytest

from conftest import assert_bash_exec


@pytest.mark.bashcomp(pre_cmds=("HOME=$PWD/mutt",))
class TestMutt:
    @pytest.mark.complete("mutt -")
    def test_options(self, completion):
        assert completion

    @pytest.mark.complete("mutt -F muttrc -f ", require_cmd=True, cwd="mutt")
    def test_filedir(self, completion):
        assert completion == "bar/ foo/ mail/ muttrc".split()

    @pytest.mark.complete("mutt -F muttrc -f =", require_cmd=True, cwd="mutt")
    def test_filedir_equals(self, completion):
        assert completion == "bar.mbx foo.mbx".split()

    @pytest.mark.complete("mutt -F muttrc -f +", require_cmd=True, cwd="mutt")
    def test_filedir_plus(self, completion):
        assert completion == "bar.mbx foo.mbx".split()

    @pytest.mark.complete("mutt -F muttrc -f =f", require_cmd=True, cwd="mutt")
    def test_equals_is_not_eaten(self, completion):
        assert completion == "oo.mbx".split()

    @pytest.mark.complete("mutt -F muttrc -f +f", require_cmd=True, cwd="mutt")
    def test_plus_is_not_eaten(self, completion):
        assert completion == "oo.mbx".split()

    @pytest.mark.complete("mutt -F muttrc -A ", cwd="mutt")
    def test_aliases(self, completion):
        assert completion == "a1 a2".split()

    def test_muttconffiles(self, bash):
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
            f"{bash.cwd}/mutt/{x}"
            for x in ("muttrc", "bar/muttrc_b", "foo/muttrc_f")
        ]

    def test_muttrc(self, bash):
        output = assert_bash_exec(
            bash,
            "(muttcmd=mutt words=-Fmutt/muttrc _muttrc); echo",
            want_output=True)
        assert output.strip() == "mutt/muttrc"

    def test_muttconfvar(self, bash):
        output = assert_bash_exec(
            bash,
            '(muttcmd=mutt words=-Fmutt/muttrc _muttconfvar folder)',
            want_output=True)
        assert output.strip() == "%s/mutt/mail" % bash.cwd
