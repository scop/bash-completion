import pytest

from conftest import assert_bash_exec


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

    @pytest.mark.complete("xspec1 ", cwd="_filedir_xspec")
    def test_1(self, functions, completion):
        """Test the pattern for an extension"""
        assert completion == sorted("a.txt b.TXT".split())

    @pytest.mark.complete("xspec2 ", cwd="_filedir_xspec")
    def test_2(self, functions, completion):
        """Test an empty _comp_xspecs entry"""
        assert completion == sorted("a.txt b.TXT c.dat d.bin".split())

    @pytest.mark.complete("xspec3 ", cwd="_filedir_xspec")
    def test_3(self, functions, completion):
        """Test an unset _comp_xspecs entry"""
        assert completion == sorted("a.txt b.TXT c.dat d.bin".split())

    @pytest.mark.complete("xspec4 ", cwd="_filedir_xspec")
    def test_4(self, functions, completion):
        """Test an exclusion pattern"""
        assert completion == sorted("c.dat d.bin".split())
