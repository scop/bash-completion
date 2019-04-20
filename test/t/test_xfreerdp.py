import pytest

from conftest import assert_bash_exec


class TestXfreerdp:
    def _help(self, bash):
        return assert_bash_exec(bash, "xfreerdp --help || :", want_output=True)

    @pytest.fixture(scope="class")
    def slash_syntax(self, bash):
        if "/help" not in self._help(bash):
            pytest.skip("Not slash syntax")

    @pytest.fixture(scope="class")
    def dash_syntax(self, bash):
        if "/help" in self._help(bash):
            pytest.skip("Not dash syntax")

    @pytest.mark.complete("xfreerdp /")
    def test_1(self, bash, completion, slash_syntax):
        assert completion

    @pytest.mark.complete("xfreerdp -")
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete("xfreerdp +")
    def test_3(self, bash, completion, slash_syntax):
        assert completion

    @pytest.mark.complete("xfreerdp /kbd:")
    def test_4(self, bash, completion, slash_syntax):
        assert completion

    @pytest.mark.complete("xfreerdp /help ")
    def test_5(self, completion):
        assert not completion

    @pytest.mark.complete("xfreerdp -k ")
    def test_6(self, bash, completion, dash_syntax):
        assert completion

    @pytest.mark.complete("xfreerdp --help ")
    def test_7(self, completion):
        assert not completion
