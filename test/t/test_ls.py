import pytest

from conftest import (
    assert_bash_exec,
    assert_complete,
    find_unique_completion_pair,
)


class TestLs:
    @pytest.mark.complete(
        "ls --", require_cmd=True, xfail="! ls --help &>/dev/null"
    )
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("ls ~")
    def test_2(self, completion):
        assert completion

    def test_3(self, bash):
        """~part should complete to ~full<SPACE> if home dir does not exist."""
        res = (
            assert_bash_exec(
                bash,
                "for u in $(compgen -u); do "
                "eval test -d ~$u || echo $u; unset u; done",
                want_output=True,
            )
            .strip()
            .split()
        )
        part_full = find_unique_completion_pair(res)
        if not part_full:
            pytest.skip("No suitable test user found")
            return
        part, full = part_full
        completion = assert_complete(bash, "ls ~%s" % part)
        assert completion == full[len(part) :]
        assert completion.endswith(" ")
