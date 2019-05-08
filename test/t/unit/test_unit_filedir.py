import pytest

from conftest import assert_bash_exec, assert_complete


@pytest.mark.bashcomp(cmd=None, ignore_env=r"^\+COMPREPLY=")
class TestUnitFiledir:
    @pytest.fixture(scope="class")
    def functions(self, request, bash):
        assert_bash_exec(
            bash,
            "_f() { local cur=$(_get_cword); unset COMPREPLY; _filedir; }; "
            "complete -F _f f; "
            "complete -F _f -o filenames f2",
        )
        assert_bash_exec(
            bash,
            "_g() { local cur=$(_get_cword); unset COMPREPLY; _filedir e1; }; "
            "complete -F _g g",
        )
        assert_bash_exec(
            bash,
            "_fd() { local cur=$(_get_cword); unset COMPREPLY; _filedir -d; };"
            "complete -F _fd fd",
        )

    def test_1(self, bash):
        assert_bash_exec(bash, "_filedir >/dev/null")

    @pytest.mark.parametrize("funcname", "f f2".split())
    def test_2(self, bash, functions, funcname):
        completion = assert_complete(bash, "%s ab/" % funcname, cwd="_filedir")
        assert completion == "ab/e"

    @pytest.mark.parametrize("funcname", "f f2".split())
    def test_3(self, bash, functions, funcname):
        completion = assert_complete(
            bash, r"%s a\ b/" % funcname, cwd="_filedir"
        )
        assert completion == "a b/i"

    @pytest.mark.parametrize("funcname", "f f2".split())
    def test_4(self, bash, functions, funcname):
        completion = assert_complete(
            bash, r"%s a\'b/" % funcname, cwd="_filedir"
        )
        assert completion == "a'b/c"

    @pytest.mark.parametrize("funcname", "f f2".split())
    def test_5(self, bash, functions, funcname):
        completion = assert_complete(
            bash, r"%s a\&b/" % funcname, cwd="_filedir"
        )
        assert completion == "a&b/f"

    @pytest.mark.parametrize("funcname", "f f2".split())
    def test_6(self, bash, functions, funcname):
        completion = assert_complete(
            bash, r"%s a\$" % funcname, cwd="_filedir"
        )
        assert completion == "a$b/"

    @pytest.mark.parametrize("funcname", "f f2".split())
    def test_7(self, bash, functions, funcname):
        completion = assert_complete(
            bash, r"%s 'ab/" % funcname, cwd="_filedir"
        )
        assert completion == "ab/e"

    @pytest.mark.parametrize("funcname", "f f2".split())
    def test_8(self, bash, functions, funcname):
        completion = assert_complete(
            bash, r"%s 'a b/" % funcname, cwd="_filedir"
        )
        assert completion == "a b/i"

    @pytest.mark.parametrize("funcname", "f f2".split())
    def test_9(self, bash, functions, funcname):
        completion = assert_complete(
            bash, r"%s 'a$b/" % funcname, cwd="_filedir"
        )
        assert completion == "a$b/h"

    @pytest.mark.parametrize("funcname", "f f2".split())
    def test_10(self, bash, functions, funcname):
        completion = assert_complete(
            bash, r"%s 'a&b/" % funcname, cwd="_filedir"
        )
        assert completion == "a&b/f"

    @pytest.mark.parametrize("funcname", "f f2".split())
    def test_11(self, bash, functions, funcname):
        completion = assert_complete(
            bash, r'%s "ab/' % funcname, cwd="_filedir"
        )
        assert completion == "ab/e"

    @pytest.mark.parametrize("funcname", "f f2".split())
    def test_12(self, bash, functions, funcname):
        completion = assert_complete(
            bash, r'%s "a b/' % funcname, cwd="_filedir"
        )
        assert completion == "a b/i"

    @pytest.mark.parametrize("funcname", "f f2".split())
    def test_13(self, bash, functions, funcname):
        completion = assert_complete(
            bash, "%s \"a'b/" % funcname, cwd="_filedir"
        )
        assert completion == "a'b/c"

    @pytest.mark.parametrize("funcname", "f f2".split())
    def test_14(self, bash, functions, funcname):
        completion = assert_complete(
            bash, '%s "a&b/' % funcname, cwd="_filedir"
        )
        assert completion == "a&b/f"

    @pytest.mark.complete(r"fd a\ ", cwd="_filedir")
    def test_15(self, functions, completion):
        assert completion == "a b/"

    @pytest.mark.complete("g ", cwd="_filedir/ext")
    def test_16(self, functions, completion):
        assert completion == sorted("ee.e1 foo/ gg.e1 ii.E1".split())
