import pytest

from conftest import assert_bash_exec


@pytest.mark.bashcomp(pre_cmds=("HOME=$PWD/mutt",))
class TestMutt:
    @pytest.fixture(scope="class")
    def functions(self, bash):
        assert_bash_exec(
            bash,
            '_comp_test__muttconffiles() { local REPLY; _comp_cmd_mutt__get_conffiles "$@" && printf "%s\\n" "${REPLY[@]}"; }',
        )

    @pytest.mark.complete("mutt -")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("mutt -F muttrc -f =", require_cmd=True, cwd="mutt")
    def test_2(self, completion):
        assert completion == "bar/ foo/ muttrc".split()

    @pytest.mark.complete("mutt -F muttrc -A ", cwd="mutt")
    def test_3(self, completion):
        assert completion == "a1 a2".split()

    def test_4(self, bash, functions):
        got = (
            assert_bash_exec(
                bash,
                '_comp_test__muttconffiles "$HOME/muttrc" "$HOME/muttrc"',
                want_output=True,
            )
            .strip()
            .split()
        )
        assert got == [
            f"{bash.cwd}/mutt/{x}"
            for x in ("muttrc", "bar/muttrc_b", "foo/muttrc_f")
        ]
