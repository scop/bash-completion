import pytest

from conftest import assert_bash_exec, assert_complete


class TestAdb:
    @pytest.mark.complete("adb ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("adb -", require_cmd=True)
    def test_2(self, completion):
        assert completion


@pytest.mark.bashcomp(cmd="adb")
class TestAdbHelp:
    @pytest.fixture(params=("modern", "legacy"))
    def adb(self, request, bash):
        cmd = "_mock_adb_" + request.param
        assert_bash_exec(
            bash, "%s() { cat adb/%s-help.txt; }" % (cmd, request.param)
        )
        assert_bash_exec(bash, "complete -F _comp_cmd_adb " + cmd)
        return cmd

    def test_commands(self, bash, adb):
        assert assert_complete(bash, adb + " ") == sorted(
            "-a -d -e -s connect devices disconnect forward help install "
            "install-multi-package install-multiple pull push reboot "
            "shell sideload version".split()
        )

    def test_install(self, bash, adb):
        assert assert_complete(bash, adb + " ins") == sorted(
            "install install-multi-package install-multiple".split()
        )

    def test_options(self, bash, adb):
        assert assert_complete(bash, adb + " -") == "-a -d -e -s".split()

    def test_unknown(self, bash, adb):
        assert not assert_complete(bash, adb + " nonexistent")

    def test_subcommand(self, bash, adb):
        assert assert_complete(bash, adb + " reboot ") == [
            "bootloader",
            "recovery",
        ]
