import pytest

from conftest import assert_complete, partialize


@pytest.mark.bashcomp(pre_cmds=("HOME=$PWD",))
class TestXhost:
    @pytest.mark.parametrize("prefix", ["+", "-", ""])
    def test_hosts(self, bash, hosts, prefix):
        completion = assert_complete(bash, "xhost %s" % prefix)
        assert completion == ["%s%s" % (prefix, x) for x in hosts]

    @pytest.mark.parametrize("prefix", ["+", "-", ""])
    def test_partial_hosts(self, bash, hosts, prefix):
        first_char, partial_hosts = partialize(bash, hosts)
        completion = assert_complete(bash, "xhost %s%s" % (prefix, first_char))
        assert completion == sorted(x[1:] for x in partial_hosts)
