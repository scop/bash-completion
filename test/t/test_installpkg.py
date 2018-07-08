import fnmatch
import os

import pytest


class TestInstallpkg(object):

    @pytest.mark.complete("installpkg -")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("installpkg --")
    def test_2(self, completion):
        assert completion.list == "--ask --infobox --md5sum --menu " \
            "--priority --root --tagfile --terse --warn".split()

    @pytest.mark.complete("installpkg --root ")
    def test_3(self, completion):
        dirs = sorted(x for x in os.listdir(".") if os.path.isdir("./%s" % x))
        assert completion.list == ["%s/" % x for x in dirs]

    @pytest.mark.complete("installpkg --root ")
    def test_4(self, completion):
        expected = sorted(
            x for x in os.listdir("slackware/home")
            if os.path.isdir("./%s" % x)
            or (os.path.isfile("./%s" % x)
                and fnmatch.fnmatch(x, "*.t[bglx]z"))
        )
        assert completion.list == expected
