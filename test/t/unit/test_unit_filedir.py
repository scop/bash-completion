import os
import shutil
import sys
import tempfile
from pathlib import Path

import pytest

from conftest import assert_bash_exec, assert_complete


@pytest.mark.bashcomp(cmd=None, ignore_env=r"^\+COMPREPLY=")
class TestUnitFiledir:
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
            "_fd() { local cur;_comp_get_words cur; unset -v COMPREPLY; _comp_compgen_filedir -d; };"
            "complete -F _fd fd",
        )

    @pytest.fixture(scope="class")
    def non_windows_testdir(self, request, bash):
        if sys.platform.startswith("win"):
            pytest.skip("Filenames not allowed on Windows")
        tempdir = Path(tempfile.mkdtemp(prefix="bash-completion_filedir"))
        request.addfinalizer(lambda: shutil.rmtree(str(tempdir)))
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
        assert_bash_exec(bash, "_comp_compgen_filedir >/dev/null")

    @pytest.mark.parametrize("funcname", "f f2".split())
    def test_2(self, bash, functions, funcname):
        completion = assert_complete(bash, "%s ab/" % funcname, cwd="_filedir")
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
        assert completion == 'h"'

    @pytest.mark.xfail(reason="TODO: non-ASCII issues with test suite?")
    @pytest.mark.parametrize("funcname", "f f2".split())
    def test_27(self, bash, functions, funcname, utf8_ctype):
        completion = assert_complete(bash, "%s aé/" % funcname, cwd="_filedir")
        assert completion == "g"
