import os

import pytest

from conftest import assert_complete


class TestMake:
    @pytest.mark.complete("make -f Ma", cwd="make")
    def test_1(self, completion):
        assert completion == "kefile"

    @pytest.mark.complete("make .", cwd="make", require_cmd=True)
    def test_2(self, bash, completion):
        """Hidden targets."""
        assert completion == ".cache/ .test_passes".split()
        os.remove(f"{bash.cwd}/make/extra_makefile")

    @pytest.mark.complete("make .cache/", cwd="make", require_cmd=True)
    def test_3(self, bash, completion):
        assert completion == "1 2".split()
        os.remove(f"{bash.cwd}/make/extra_makefile")

    @pytest.mark.complete("make ", cwd="shared/empty_dir")
    def test_4(self, completion):
        assert not completion

    @pytest.mark.complete("make -j ")
    def test_5(self, completion):
        assert completion

    @pytest.mark.complete("make ", cwd="make", require_cmd=True)
    def test_6(self, bash, completion):
        assert completion == "all clean extra_makefile install sample".split()
        os.remove(f"{bash.cwd}/make/extra_makefile")

    @pytest.mark.complete("make .cache/.", cwd="make", require_cmd=True)
    def test_7(self, bash, completion):
        assert completion == ".1 .2".split()
        os.remove(f"{bash.cwd}/make/extra_makefile")

    @pytest.mark.complete("make -C make ", require_cmd=True)
    def test_8(self, bash, completion):
        assert completion == "all clean extra_makefile install sample".split()
        os.remove(f"{bash.cwd}/make/extra_makefile")

    @pytest.mark.complete("make -", require_cmd=True)
    def test_9(self, completion):
        assert completion


@pytest.mark.bashcomp(require_cmd=True, temp_cwd=True)
class TestMake2:
    def test_github_issue_544_1(self, bash):
        print(os.getcwd())
        print(bash.cwd)
        with open("Makefile", "w") as f:
            f.write(
                "all: abc/xyz\n"
                ".PHONY: abc/xyz\n"
                "abc/xyz 123/xaa 123/xbb:\n"
                "\tmkdir -p $(@:/%=)\n"
                "\tdate > $@\n"
            )
        completion = assert_complete(bash, "make ab")
        assert completion == "c/xyz"

    def test_github_issue_544_2(self, bash):
        completion = assert_complete(bash, "make 1")
        assert completion == "23/"

    def test_github_issue_544_3(self, bash):
        completion = assert_complete(bash, "make 123/")
        assert completion == ["xaa", "xbb"]

    def test_github_issue_544_4(self, bash):
        completion = assert_complete(bash, "make 123/xa")
        assert completion == "a"
