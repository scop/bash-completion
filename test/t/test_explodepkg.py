import fnmatch
import os

import pytest


class TestExplodepkg:
    @pytest.mark.complete("explodepkg ", cwd="slackware/home")
    def test_1(self, completion):
        expected = sorted(
            x
            for x in os.listdir("slackware/home")
            if os.path.isdir("./%s" % x)
            or (
                os.path.isfile("./%s" % x) and fnmatch.fnmatch(x, "*.t[bglx]z")
            )
        )
        assert completion == expected
