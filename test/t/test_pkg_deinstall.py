import os

import pytest


@pytest.mark.pre_commands(
    "PKG_DBDIR=pkgtools/db",
)
class Test(object):

    @pytest.mark.complete("pkg_deinstall ")
    def test_pkgs(self, completion):
        dirs = sorted(x for x in os.listdir("pkgtools/db")
                      if os.path.isdir("pkgtools/db/%s" % x))
        assert completion.list == dirs
