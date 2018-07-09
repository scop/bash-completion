import subprocess

import pytest


class TestModinfo(object):

    @pytest.mark.complete("modinfo -")
    def test_1(self, completion):
        assert completion.list

    # "in": intel*, ...
    @pytest.mark.complete("modinfo in",
                          skipif="! ls /lib/modules/%s &>/dev/null" %
                          subprocess.check_output(
                              "uname -r 2>/dev/null || "
                              "echo non-existent-kernel",
                              shell=True).decode().strip())
    def test_2(self, completion):
        assert completion.list

    # "in": intel*, ...
    @pytest.mark.complete("modinfo -k non-existent-kernel in")
    def test_3(self, completion):
        assert not completion.list

    @pytest.mark.complete("modinfo /tm")
    def test_4(self, completion):
        assert completion.list
        assert not completion.line.endswith(" ")
