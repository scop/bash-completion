import pytest

from conftest import assert_bash_exec


class TestXfreerdp:
    def _help(self, bash):
        return assert_bash_exec(
            bash, "xfreerdp --help 2>&1 || :", want_output=True
        )

    @pytest.fixture(scope="class")
    def help_success(self, bash):
        output = self._help(bash)
        # Example from our CentOS 7 container
        # [04:51:31:663] [238:238] [ERROR][com.freerdp.client.x11] - Failed to get pixmap info
        if not output or "ERROR" in output.strip().splitlines()[0]:
            pytest.skip("--help errored")

    @pytest.fixture(scope="class")
    def slash_syntax(self, bash, help_success):
        if "/help" not in self._help(bash):
            pytest.skip("Not slash syntax")

    @pytest.fixture(scope="class")
    def dash_syntax(self, bash):
        if "/help" in self._help(bash):
            pytest.skip("Not dash syntax")

    @pytest.mark.complete("xfreerdp /", require_cmd=True)
    def test_1(self, bash, completion, help_success, slash_syntax):
        assert completion

    @pytest.mark.complete("xfreerdp -", require_cmd=True)
    def test_2(self, completion, help_success):
        assert completion

    @pytest.mark.complete("xfreerdp +", require_cmd=True)
    def test_3(self, bash, completion, help_success, slash_syntax):
        assert completion

    @pytest.mark.complete(
        "xfreerdp /kbd:",
        require_cmd=True,
        skipif='test -z "$(xfreerdp /kbd-list 2>/dev/null)"',
    )
    def test_4(self, bash, completion, help_success, slash_syntax):
        assert completion

    @pytest.mark.complete("xfreerdp /help ", require_cmd=True)
    def test_5(self, completion, help_success):
        assert not completion

    @pytest.mark.complete("xfreerdp -k ", require_cmd=True)
    def test_6(self, bash, completion, help_success, dash_syntax):
        assert completion

    @pytest.mark.complete("xfreerdp --help ", require_cmd=True)
    def test_7(self, completion):
        assert not completion
