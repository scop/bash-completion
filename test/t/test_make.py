import os

import pytest


class TestMake:

    @pytest.mark.complete("make -f Ma", cwd="make")
    def test_1(self, completion):
        assert completion.list == ["Makefile"]

    @pytest.mark.complete("make .", cwd="make")
    def test_2(self, bash, completion):
        """Hidden targets."""
        assert completion.list == ".cache/ .test_passes".split()
        os.remove("%s/make/%s" % (bash.cwd, "extra_makefile"))

    @pytest.mark.complete("make .cache/", cwd="make")
    def test_3(self, bash, completion):
        assert completion.list == "1 2".split()
        os.remove("%s/make/%s" % (bash.cwd, "extra_makefile"))

    @pytest.mark.complete("make ", cwd="shared/empty_dir")
    def test_4(self, completion):
        assert not completion.list

    @pytest.mark.complete("make -j ")
    def test_5(self, completion):
        assert completion.list

    @pytest.mark.complete("make ", cwd="make")
    def test_6(self, bash, completion):
        assert completion.list == \
            "all clean extra_makefile install sample".split()
        os.remove("%s/make/%s" % (bash.cwd, "extra_makefile"))

    @pytest.mark.xfail(
        bool(os.environ.get("CI")) and os.environ.get("DIST") == "centos6",
        reason="Fails for some unknown reason on CentOS 6, even though "
        "the behavior appears to be correct")
    @pytest.mark.complete("make .cache/.", cwd="make")
    def test_7(self, bash, completion):
        assert completion.list == ".1 .2".split()
        os.remove("%s/make/%s" % (bash.cwd, "extra_makefile"))
