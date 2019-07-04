import fnmatch
import os

import pytest


class TestExplodepkg:
    @pytest.mark.complete("explodepkg ", cwd="slackware/home")
    def test_1(self, completion):
        expected = sorted(
            [
                "%s/" % x
                for x in os.listdir("slackware/home")
                if os.path.isdir("./slackware/home/%s" % x)
            ]
            + [
                x
                for x in os.listdir("slackware/home")
                if os.path.isfile("./slackware/home/%s" % x)
                and fnmatch.fnmatch(x, "*.t[bglx]z")
            ]
        )
        assert completion == expected
