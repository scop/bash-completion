import pytest

from conftest import assert_complete


class TestIpmitool:
    @pytest.mark.complete("ipmitool ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("ipmitool -", require_cmd=True)
    def test_2(self, completion):
        assert completion

    @pytest.mark.parametrize("cmd", "lan sdr sensor sel user".split())
    def test_subcommands(self, bash, cmd):
        completion = assert_complete(bash, "ipmitool %s " % cmd)
        assert completion
