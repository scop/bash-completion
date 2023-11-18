import fnmatch
import os

import pytest


class TestInstallpkg:
    @pytest.mark.complete("installpkg -")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("installpkg --")
    def test_2(self, completion):
        assert (
            completion
            == "--ask --infobox --md5sum --menu "
            "--priority --root --tagfile --terse --warn".split()
        )

    @pytest.mark.complete("installpkg --root ")
    def test_3(self, completion):
        dirs = sorted(x for x in os.listdir(".") if os.path.isdir("./%s" % x))
        assert completion == ["%s/" % x for x in dirs]

    @pytest.mark.complete("installpkg ", cwd="slackware/home")
    def test_4(self, completion):
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
