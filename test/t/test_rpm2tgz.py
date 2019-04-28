import os

import pytest


class TestRpm2tgz:
    @pytest.mark.complete("rpm2tgz -")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("rpm2tgz ", cwd="slackware/home")
    def test_2(self, completion):
        expected = sorted(
            [
                "%s/" % x
                for x in os.listdir("slackware/home")
                if os.path.isdir("slackware/home/%s" % x)
            ]
            + [
                x
                for x in os.listdir("slackware/home")
                if os.path.isfile("slackware/home/%s" % x)
                and x.endswith(".rpm")
            ]
        )
        assert completion == expected
