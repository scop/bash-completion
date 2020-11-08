import pytest

from conftest import assert_bash_exec


@pytest.mark.bashcomp(cmd=None, ignore_env=r"^\+(COMPREPLY|cur)=")
class TestUnitPgids:
    def test_smoke(self, bash):
        assert_bash_exec(bash, "cur=; _pgids >/dev/null")

    def test_non_pollution(self, bash):
        """Test environment non-pollution, detected at teardown."""
        assert_bash_exec(bash, "foo() { local cur=; _pgids; }; foo; unset foo")

    def test_ints(self, bash):
        """Test that we get something, and only ints."""
        completion = assert_bash_exec(
            bash,
            r'cur=; _pgids; printf "%s\n" "${COMPREPLY[@]}"',
            want_output=True,
        ).split()
        assert completion
        assert all(x.isdigit() for x in completion)
