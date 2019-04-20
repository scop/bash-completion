import os

import pytest


@pytest.mark.bashcomp(pre_cmds=("PKG_DBDIR=$PWD/pkgtools/db",))
class TestPkgDeinstall:
    @pytest.mark.complete("pkg_deinstall ")
    def test_1(self, completion):
        dirs = sorted(
            x
            for x in os.listdir("pkgtools/db")
            if os.path.isdir("pkgtools/db/%s" % x)
        )
        assert completion == dirs
