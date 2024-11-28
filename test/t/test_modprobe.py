import subprocess

import pytest


class TestModprobe:
    @pytest.mark.complete("modprobe --al")
    def test_1(self, completion):
        assert completion == "l"

    # "du": dummy, ...
    @pytest.mark.complete(
        "modprobe du",
        xfail="! ls /lib/modules/%s &>/dev/null"
        % subprocess.check_output(
            "uname -r 2>/dev/null || " "echo non-existent-kernel", shell=True
        )
        .decode()
        .strip(),
    )
    def test_2(self, completion):
        assert completion

    # "du": dummy, ...
    @pytest.mark.complete("modprobe -S non-existent-kernel du")
    def test_3(self, completion):
        assert not completion

    @pytest.mark.complete("modprobe non-existent-module ")
    def test_4(self, completion):
        assert not completion

    @pytest.mark.complete("modprobe /tm")
    def test_5(self, completion):
        assert completion
        assert not completion.endswith(" ")
