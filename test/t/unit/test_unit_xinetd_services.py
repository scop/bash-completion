import pytest

from conftest import assert_bash_exec


@pytest.mark.bashcomp(cmd=None, ignore_env=r"^\+COMPREPLY=")
class TestUnitXinetdServices:
    def test_direct(self, bash):
        assert_bash_exec(bash, "_xinetd_services >/dev/null")

    def test_env_non_pollution(self, bash):
        """Test environment non-pollution, detected at teardown."""
        assert_bash_exec(
            bash, "foo() { _xinetd_services; }; foo; unset -f foo"
        )

    def test_basic(self, bash):
        output = assert_bash_exec(
            bash,
            "foo() { local _comp_test_xinetd_dir=$PWD/shared/bin; unset -v COMPREPLY; "
            '_xinetd_services; printf "%s\\n" "${COMPREPLY[@]}"; }; foo; unset -f foo',
            want_output=True,
        )
        assert sorted(output.split()) == ["arp", "ifconfig"]
