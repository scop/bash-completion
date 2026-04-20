import os
import sys

import pytest

from conftest import assert_bash_exec, assert_complete, bash_env_saved


@pytest.mark.bashcomp(cmd=None, ignore_env=r"^\+COMPREPLY=")
class TestUnitCompgenFiledir:
    @pytest.fixture(scope="class")
    def functions(self, request, bash):
        assert_bash_exec(
            bash,
            "_f() { local cur;_comp_get_words cur; unset -v COMPREPLY; _comp_compgen_filedir; }; "
            "complete -F _f f; "
            "complete -F _f -o filenames f2",
        )
        assert_bash_exec(
            bash,
            "_g() { local cur;_comp_get_words cur; unset -v COMPREPLY; _comp_compgen_filedir e1; }; "
            "complete -F _g g",
        )
        assert_bash_exec(
            bash,
            "_fc() { local cur=$(_get_cword); unset -v COMPREPLY; _comp_compgen -C _filedir filedir; }; "
            "complete -F _fc fc; "
            "complete -F _fc -o filenames fc2",
        )
        assert_bash_exec(
            bash,
            "_fd() { local cur;_comp_get_words cur; unset -v COMPREPLY; _comp_compgen_filedir -d; };"
            "complete -F _fd fd",
        )
        assert_bash_exec(
            bash,
            "_fcd() { local cur=$(_get_cword); unset -v COMPREPLY; _comp_compgen -C _filedir filedir -d; };"
            "complete -F _fcd fcd",
        )

    @pytest.fixture(scope="class")
    def non_windows_testdir(self, bash, tmp_path_factory):
        if sys.platform.startswith("win"):
            pytest.skip("Filenames not allowed on Windows")
        tempdir = tmp_path_factory.mktemp(
            "bash-completion._comp_compgen_filedir."
        )
        subdir = tempdir / 'a"b'
        subdir.mkdir()
        (subdir / "d").touch()
        subdir = tempdir / "a*b"
        subdir.mkdir()
        (subdir / "j").touch()
        subdir = tempdir / r"a\b"
        subdir.mkdir()
        (subdir / "g").touch()
        return tempdir

    @pytest.fixture(scope="class")
    def utf8_ctype(self, bash):
        # TODO: this likely is not the right thing to do. Instead we should
        # grab the setting from the running shell, possibly eval $(locale)
        # in a subshell and grab LC_CTYPE from there. That doesn't seem to work
        # either everywhere though.
        lc_ctype = os.environ.get("LC_CTYPE", "")
        if "UTF-8" not in lc_ctype:
            pytest.skip("Applicable only in LC_CTYPE=UTF-8 setups")
        return lc_ctype

    def test_1(self, bash):
        with bash_env_saved(bash) as bash_env:
            bash_env.write_variable("cur", "")
            assert_bash_exec(bash, 'cur="" _comp_compgen_filedir >/dev/null')

    @pytest.mark.parametrize("funcname", "f f2".split())
    def test_2(self, bash, functions, funcname):
        completion = assert_complete(bash, "%s ab/" % funcname, cwd="_filedir")
        assert completion == "e"

    @pytest.mark.parametrize("funcname", "fc fc2".split())
    def test_2C(self, bash, functions, funcname):
        completion = assert_complete(bash, "%s _filedir ab/" % funcname)
        assert completion == "e"

    @pytest.mark.parametrize("funcname", "f f2".split())
    def test_3(self, bash, functions, funcname):
        completion = assert_complete(
            bash, r"%s a\ b/" % funcname, cwd="_filedir"
        )
        assert completion == "i"

    @pytest.mark.parametrize("funcname", "f f2".split())
    def test_4(self, bash, functions, funcname):
        completion = assert_complete(
            bash, r"%s a\'b/" % funcname, cwd="_filedir"
        )
        assert completion == "c"

    @pytest.mark.parametrize("funcname", "f f2".split())
    def test_5(self, bash, functions, funcname):
        completion = assert_complete(
            bash, r"%s a\&b/" % funcname, cwd="_filedir"
        )
        assert completion == "f"

    @pytest.mark.parametrize("funcname", "f f2".split())
    def test_6(self, bash, functions, funcname):
        completion = assert_complete(
            bash, r"%s a\$" % funcname, cwd="_filedir"
        )
        assert completion == "b/"

    @pytest.mark.parametrize("funcname", "f f2".split())
    def test_7(self, bash, functions, funcname):
        completion = assert_complete(
            bash, r"%s 'ab/" % funcname, cwd="_filedir"
        )
        assert completion == "e'"

    @pytest.mark.parametrize("funcname", "f f2".split())
    def test_8(self, bash, functions, funcname):
        completion = assert_complete(
            bash, r"%s 'a b/" % funcname, cwd="_filedir"
        )
        assert completion == "i'"

    @pytest.mark.parametrize("funcname", "f f2".split())
    def test_9(self, bash, functions, funcname):
        completion = assert_complete(
            bash, r"%s 'a$b/" % funcname, cwd="_filedir"
        )
        assert completion == "h'"

    @pytest.mark.parametrize("funcname", "f f2".split())
    def test_10(self, bash, functions, funcname):
        completion = assert_complete(
            bash, r"%s 'a&b/" % funcname, cwd="_filedir"
        )
        assert completion == "f'"

    @pytest.mark.parametrize("funcname", "f f2".split())
    def test_11(self, bash, functions, funcname):
        completion = assert_complete(
            bash, r'%s "ab/' % funcname, cwd="_filedir"
        )
        assert completion == 'e"'

    @pytest.mark.parametrize("funcname", "f f2".split())
    def test_12(self, bash, functions, funcname):
        completion = assert_complete(
            bash, r'%s "a b/' % funcname, cwd="_filedir"
        )
        assert completion == 'i"'

    @pytest.mark.parametrize("funcname", "f f2".split())
    def test_13(self, bash, functions, funcname):
        completion = assert_complete(
            bash, "%s \"a'b/" % funcname, cwd="_filedir"
        )
        assert completion == 'c"'

    @pytest.mark.parametrize("funcname", "f f2".split())
    def test_14(self, bash, functions, funcname):
        completion = assert_complete(
            bash, '%s "a&b/' % funcname, cwd="_filedir"
        )
        assert completion == 'f"'

    @pytest.mark.complete(r"fd a\ ", cwd="_filedir")
    def test_15(self, functions, completion):
        assert completion == "b/"

    @pytest.mark.complete(r"fcd a\ ")
    def test_15d(self, functions, completion):
        assert completion == "b/"

    @pytest.mark.complete("g ", cwd="_filedir/ext")
    def test_16(self, functions, completion):
        assert completion == sorted("ee.e1 foo/ gg.e1 ii.E1".split())

    @pytest.mark.parametrize("funcname", "f f2".split())
    def test_17(self, bash, functions, funcname):
        completion = assert_complete(
            bash, r"%s a\$b/" % funcname, cwd="_filedir"
        )
        assert completion == "h"

    @pytest.mark.parametrize("funcname", "f f2".split())
    def test_18(self, bash, functions, funcname):
        completion = assert_complete(
            bash, r"%s \[x" % funcname, cwd="_filedir/brackets"
        )
        assert completion == r"\]"

    @pytest.mark.parametrize("funcname", "f f2".split())
    def test_19(self, bash, functions, funcname, non_windows_testdir):
        completion = assert_complete(
            bash, '%s a\\"b/' % funcname, cwd=non_windows_testdir
        )
        assert completion == "d"

    @pytest.mark.parametrize("funcname", "f f2".split())
    def test_20(self, bash, functions, funcname, non_windows_testdir):
        completion = assert_complete(
            bash, r"%s a\\b/" % funcname, cwd=non_windows_testdir
        )
        assert completion == "g"

    @pytest.mark.parametrize("funcname", "f f2".split())
    def test_21(self, bash, functions, funcname, non_windows_testdir):
        completion = assert_complete(
            bash, "%s 'a\"b/" % funcname, cwd=non_windows_testdir
        )
        assert completion == "d'"

    @pytest.mark.parametrize("funcname", "f f2".split())
    def test_22(self, bash, functions, funcname, non_windows_testdir):
        completion = assert_complete(
            bash, rf"{funcname} '{non_windows_testdir}/a\b/"
        )
        assert completion == "g'"

    @pytest.mark.parametrize("funcname", "f f2".split())
    def test_23(self, bash, functions, funcname, non_windows_testdir):
        completion = assert_complete(
            bash, r'%s "a\"b/' % funcname, cwd=non_windows_testdir
        )
        assert completion == 'd"'

    @pytest.mark.parametrize("funcname", "f f2".split())
    def test_24(self, bash, functions, funcname, non_windows_testdir):
        completion = assert_complete(
            bash, r'%s "a\\b/' % funcname, cwd=non_windows_testdir
        )
        assert completion == 'g"'

    @pytest.mark.parametrize("funcname", "f f2".split())
    def test_25(self, bash, functions, funcname):
        completion = assert_complete(
            bash, r'%s "a\b/' % funcname, cwd="_filedir"
        )
        assert completion == '\b\b\bb/e"'

    @pytest.mark.parametrize("funcname", "f f2".split())
    def test_26(self, bash, functions, funcname):
        completion = assert_complete(
            bash, r'%s "a\$b/' % funcname, cwd="_filedir"
        )
        try:
            assert completion == 'h"'
        except AssertionError:
            bash_version = assert_bash_exec(
                bash,
                r'printf "%s.%s\n" "${BASH_VERSINFO[0]}" "${BASH_VERSINFO[1]}"',
                want_output=True,
            ).strip()
            # This is workaround for https://github.com/scop/bash-completion/issues/1435, see
            # https://lists.gnu.org/archive/html/bug-bash/2025-09/msg00332.html
            # Once this is fixed, the version check should be minimized further
            if bash_version == "5.3":
                assert completion.endswith('h" ')
            else:
                raise

    @pytest.mark.xfail(reason="TODO: non-ASCII issues with test suite?")
    @pytest.mark.parametrize("funcname", "f f2".split())
    def test_27(self, bash, functions, funcname, utf8_ctype):
        completion = assert_complete(bash, "%s aé/" % funcname, cwd="_filedir")
        assert completion == "g"

    @pytest.mark.parametrize("funcname", "f f2".split())
    def test_28_dot_1(self, bash, functions, funcname):
        """Exclude . and .. when the completion is attempted for '.[TAB]'"""
        completion = assert_complete(bash, r"%s ." % funcname, cwd="_filedir")
        assert completion == [".dotfile1", ".dotfile2"]

    @pytest.mark.parametrize("funcname", "f f2".split())
    def test_28_dot_2(self, bash, functions, funcname):
        """Exclude . and .. when the completion is attempted for 'dir/.[TAB]'"""
        completion = assert_complete(bash, r"%s _filedir/." % funcname)
        assert completion == [".dotfile1", ".dotfile2"]

    @pytest.mark.parametrize("funcname", "f f2".split())
    def test_28_dot_3(self, bash, functions, funcname):
        """Include . when the completion is attempted for '..[TAB]'"""
        completion = assert_complete(bash, r"%s .." % funcname, cwd="_filedir")
        assert completion == "/"

    @pytest.mark.parametrize("funcname", "f f2".split())
    def test_28_dot_4(self, bash, functions, funcname):
        """Include . when the completion is attempted for '..[TAB]'"""
        completion = assert_complete(bash, r"%s _filedir/.." % funcname)
        assert completion == "/"

    @pytest.mark.parametrize("funcname", "f f2".split())
    def test_29_dotdot(self, bash, functions, funcname):
        """Complete files starting with "..".

        These types of files are used by the go kubernetes atomic writer [0],
        and presumably other types of systems, and we want to make sure they
        will be completed correctly.

        [0] https://pkg.go.dev/k8s.io/kubernetes/pkg/volume/util#AtomicWriter.Write
        """
        completion = assert_complete(
            bash, r"%s .." % funcname, cwd="_filedir/dotdot/"
        )
        assert completion == [
            "../",
            "..2016_02_01_15_04_05.123456",
            "..data",
            "..folder/",
        ]
