import os
import sys

import pytest


class TestMake:
    @pytest.fixture
    def remove_extra_makefile(self, bash):
        yield
        # For some reason macos make doesn't actually create extra_makefile
        if sys.platform != "darwin":
            os.remove(f"{bash.cwd}/make/extra_makefile")

    @pytest.mark.complete("make -f Ma", cwd="make")
    def test_1(self, completion):
        assert completion == "kefile"

    @pytest.mark.complete("make .", cwd="make", require_cmd=True)
    def test_2(self, bash, completion, remove_extra_makefile):
        """Hidden targets."""
        assert completion == ".cache/ .test_passes".split()

    @pytest.mark.complete("make .cache/", cwd="make", require_cmd=True)
    def test_3(self, bash, completion, remove_extra_makefile):
        assert completion == ".cache/1 .cache/2".split()

    @pytest.mark.complete("make ", cwd="shared/empty_dir")
    def test_4(self, completion):
        assert not completion

    @pytest.mark.complete("make -j ")
    def test_5(self, completion):
        assert completion

    @pytest.mark.complete("make ", cwd="make", require_cmd=True)
    def test_6(self, bash, completion, remove_extra_makefile):
        assert (
            completion
            == "all clean extra_makefile fluff install sample".split()
        )

    @pytest.mark.complete("make .cache/.", cwd="make", require_cmd=True)
    def test_7(self, bash, completion, remove_extra_makefile):
        assert completion == ".cache/.1 .cache/.2".split()

    @pytest.mark.complete("make -C make ", require_cmd=True)
    def test_8(self, bash, completion, remove_extra_makefile):
        assert (
            completion
            == "all clean extra_makefile fluff install sample".split()
        )

    @pytest.mark.complete("make -nC make ", require_cmd=True)
    def test_8n(self, bash, completion, remove_extra_makefile):
        assert (
            completion
            == "all clean extra_makefile fluff install sample".split()
        )

    @pytest.mark.complete("make -", require_cmd=True)
    def test_9(self, completion):
        assert completion

    @pytest.mark.complete("make f", cwd="make", require_cmd=True)
    def test_github_pr_1577_1(self, bash, completion, remove_extra_makefile):
        """The completion should not generate an unmatching target like "all",
        which appears after the "Not a target" sequence, affected by the
        leftover state for "foobar".  Otherwise, "fluff" would fail to be
        completed as the unique completion.

        https://github.com/scop/bash-completion/pull/1577
        """
        assert completion == "luff"

    @pytest.mark.complete(
        "make ba", cwd="make/test_github_pr_1577", require_cmd=True
    )
    def test_github_pr_1577_2(self, bash, completion):
        """Although the "Not a target" version of "foobar: OUCH = glitch"
        should be excluded, the version with the actual recipe should still be
        generated.
        """
        assert completion == "rbaz"


@pytest.mark.bashcomp(require_cmd=True, cwd="make/test2")
class TestMake2:
    @pytest.mark.complete("make ab")
    def test_github_issue_544_1(self, completion):
        assert completion == "c/xyz"

    @pytest.mark.complete("make 1")
    def test_github_issue_544_2(self, completion):
        assert completion == "23/"

    @pytest.mark.complete("make 123/")
    def test_github_issue_544_3(self, completion):
        assert completion == ["123/xaa", "123/xbb"]

    @pytest.mark.complete("make 123/xa")
    def test_github_issue_544_4(self, completion):
        assert completion == "a"

    @pytest.mark.complete("make sub1")
    def test_subdir_1(self, completion):
        assert completion == "test/bar/"

    @pytest.mark.complete("make sub2")
    def test_subdir_2(self, completion):
        assert completion == "test/bar/alpha"

    @pytest.mark.complete("make sub3")
    def test_subdir_3(self, completion):
        assert completion == "test/"

    @pytest.mark.complete("make sub4")
    def test_subdir_4(self, completion):
        assert completion == "sub4test/bar/ sub4test2/foo/gamma".split()


@pytest.mark.bashcomp(cmd="make", require_cmd=True, cwd="make/test3")
class TestMake3:
    """CMake-style phony targets whose names use `/' as a naming convention.

    A `/' in a target name is not necessarily a directory boundary.  `make -p'
    marks these targets phony, so the completion offers them as-is instead of
    collapsing `install' into `install/' or dropping the plain `MyProgram' in
    favor of only `MyProgram/fast'.
    """

    @pytest.mark.complete("make ")
    def test_all_targets(self, completion):
        """Phony targets are offered as-is, not collapsed as directories."""
        assert completion == [
            "MyProgram",
            "MyProgram/fast",
            "all",
            "clean",
            "clean/fast",
            "install",
            "install/local",
            "install/strip",
        ]

    @pytest.mark.complete("make My")
    def test_single_child(self, completion):
        """`MyProgram' is offered alongside `MyProgram/fast'."""
        assert completion == ["MyProgram", "MyProgram/fast"]

    @pytest.mark.complete("make MyProgram/")
    def test_single_child_drill_in(self, completion):
        assert completion == "fast"

    @pytest.mark.complete("make install")
    def test_multi_child(self, completion):
        """`install' is offered alongside `install/local', `install/strip'."""
        assert completion == ["install", "install/local", "install/strip"]

    @pytest.mark.complete("make install/")
    def test_multi_child_drill_in(self, completion):
        assert completion == ["install/local", "install/strip"]

    @pytest.mark.complete("make clean")
    def test_clean(self, completion):
        """A second single-child case: `clean' alongside `clean/fast'."""
        assert completion == ["clean", "clean/fast"]


@pytest.mark.bashcomp(cmd="make", require_cmd=True)
class TestMakeOptions:
    """Phony targets are offered as-is when the makefile or its directory is
    selected via -f/-C.

    Run from the fixtures root so the -C/-f paths are relative to it.
    """

    @pytest.mark.complete("make -C make/test3 install")
    def test_directory_option(self, completion):
        assert completion == ["install", "install/local", "install/strip"]

    @pytest.mark.complete("make -f make/test3/Makefile install")
    def test_file_option(self, completion):
        assert completion == ["install", "install/local", "install/strip"]


@pytest.mark.bashcomp(cmd="make", require_cmd=True, cwd="make/test4")
class TestMake4:
    """Non-phony targets containing `/' are real file paths, so completion
    keeps collapsing shared prefixes to `dir/' (issues #544/#858).  A
    non-phony target that is itself a directory prefix (`sub', a real
    directory built by a recipe) stays collapsed to `sub/', never surfaced
    as a plain runnable name.
    """

    @pytest.mark.complete("make ")
    def test_all_targets(self, completion):
        assert completion == ["dir/", "sub/"]

    @pytest.mark.complete("make sub")
    def test_dir_prep_target_stays_collapsed(self, completion):
        """`sub' is a real directory target, not a phony label, so it is not
        surfaced as a plain name; it stays collapsed to `sub/'."""
        assert completion == "/"
        # Collapsed `sub/' must not get a trailing space (nospace is set).
        assert completion.endswith("/")

    @pytest.mark.complete("make sub/")
    def test_dir_prep_drill_in(self, completion):
        assert completion == ["sub/a", "sub/b"]

    @pytest.mark.complete("make dir")
    def test_non_target_prefix_collapses(self, completion):
        """`dir' is not a target, only a shared prefix, so it collapses to
        `dir/'."""
        assert completion == "/"
        assert completion.endswith("/")
