import subprocess

import pytest


class TestModinfo:
    @pytest.mark.complete("modinfo -", require_cmd=True)
    def test_1(self, completion):
        assert completion

    # "in": intel*, ...
    @pytest.mark.complete(
        "modinfo in",
        xfail="! ls /lib/modules/%s &>/dev/null"
        % subprocess.check_output(
            "uname -r 2>/dev/null || " "echo non-existent-kernel", shell=True
        )
        .decode()
        .strip(),
    )
    def test_2(self, completion):
        assert completion

    # "in": intel*, ...
    @pytest.mark.complete("modinfo -k non-existent-kernel in")
    def test_3(self, completion):
        assert not completion

    @pytest.mark.complete("modinfo /tm")
    def test_4(self, completion):
        assert completion
        assert not completion.endswith(" ")
