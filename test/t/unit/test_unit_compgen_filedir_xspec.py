import pytest

from conftest import assert_bash_exec, assert_complete


@pytest.mark.bashcomp(cmd=None, ignore_env=r"^\+COMPREPLY=|^[-+]_comp_xspecs=")
class TestUnitFiledirXspec:
    @pytest.fixture(scope="class")
    def functions(self, request, bash):
        assert_bash_exec(
            bash,
            "_comp_xspecs[xspec1]='!*.txt'; "
            "_comp_xspecs[xspec2]=; "
            "_comp_xspecs[xspec4]='*.txt'; "
            "complete -F _filedir_xspec xspec{1..4}",
        )

    def test_1(self, bash, functions):
        """Test the pattern for an extension"""
        completion = assert_complete(bash, "xspec1 ", cwd="_filedir_xspec")
        assert completion == sorted("a.txt b.TXT".split())

    def test_2(self, bash, functions):
        """Test an empty _comp_xspecs entry"""
        completion = assert_complete(bash, "xspec2 ", cwd="_filedir_xspec")
        assert completion == sorted("a.txt b.TXT c.dat d.bin".split())

    def test_3(self, bash, functions):
        """Test an unset _comp_xspecs entry"""
        completion = assert_complete(bash, "xspec3 ", cwd="_filedir_xspec")
        assert completion == sorted("a.txt b.TXT c.dat d.bin".split())

    def test_4(self, bash, functions):
        """Test an exclusion pattern"""
        completion = assert_complete(bash, "xspec4 ", cwd="_filedir_xspec")
        assert completion == sorted("c.dat d.bin".split())
