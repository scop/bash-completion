import os

import pytest

from conftest import assert_bash_exec, bash_env_saved


@pytest.mark.bashcomp(cmd=None, ignore_env=r"^\+COMPREPLY=")
class TestUnitPids:
    def test_smoke(self, bash):
        with bash_env_saved(bash) as bash_env:
            bash_env.write_variable("cur", "")
            assert_bash_exec(bash, "_comp_compgen_pids >/dev/null")

    def test_non_pollution(self, bash):
        """Test environment non-pollution, detected at teardown."""
        assert_bash_exec(
            bash,
            "foo() { local cur=; _comp_compgen_pids; }; foo; unset -f foo",
        )

    def test_ints(self, bash):
        """Test that we get something sensible, and only int'y strings."""
        with bash_env_saved(bash) as bash_env:
            bash_env.write_variable("cur", "")
            completion = assert_bash_exec(
                bash,
                r'_comp_compgen_pids; printf "%s\n" "${COMPREPLY[@]}"',
                want_output=True,
            ).split()
        assert completion
        if hasattr(os, "getpid"):
            assert str(os.getpid()) in completion
        assert all(x.isdigit() for x in completion)
