import os

import pytest


class TestMake:
    @pytest.mark.complete("make -f Ma", cwd="make")
    def test_1(self, completion):
        assert completion == "kefile"

    @pytest.mark.complete("make .", cwd="make", require_cmd=True)
    def test_2(self, bash, completion):
        """Hidden targets."""
        assert completion == ".cache/ .test_passes".split()
        os.remove("%s/make/%s" % (bash.cwd, "extra_makefile"))

    @pytest.mark.complete("make .cache/", cwd="make", require_cmd=True)
    def test_3(self, bash, completion):
        assert completion == "1 2".split()
        os.remove("%s/make/%s" % (bash.cwd, "extra_makefile"))

    @pytest.mark.complete("make ", cwd="shared/empty_dir")
    def test_4(self, completion):
        assert not completion

    @pytest.mark.complete("make -j ")
    def test_5(self, completion):
        assert completion

    @pytest.mark.complete("make ", cwd="make", require_cmd=True)
    def test_6(self, bash, completion):
        assert completion == "all clean extra_makefile install sample".split()
        os.remove("%s/make/%s" % (bash.cwd, "extra_makefile"))

    @pytest.mark.complete("make .cache/.", cwd="make", require_cmd=True)
    def test_7(self, bash, completion):
        assert completion == ".1 .2".split()
        os.remove("%s/make/%s" % (bash.cwd, "extra_makefile"))

    @pytest.mark.complete("make -C make ", require_cmd=True)
    def test_8(self, bash, completion):
        assert completion == "all clean extra_makefile install sample".split()
        os.remove("%s/make/%s" % (bash.cwd, "extra_makefile"))

    @pytest.mark.complete("make -", require_cmd=True)
    def test_9(self, completion):
        assert completion
