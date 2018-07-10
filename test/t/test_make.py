import os

import pytest


class TestMake(object):

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
