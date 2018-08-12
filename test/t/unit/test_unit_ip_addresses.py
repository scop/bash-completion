import pytest

from conftest import assert_bash_exec


@pytest.mark.bashcomp(cmd=None, ignore_env=r"^\+COMPREPLY=")
class TestUnitIpAddresses:

    def test_1(self, bash):
        assert_bash_exec(bash, "_ip_addresses")
