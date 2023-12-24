import pytest

from conftest import assert_bash_exec


@pytest.mark.bashcomp(
    cmd=None, cwd="shared", ignore_env=r"^\+declare -f __tester$"
)
class TestUnitAbsPath:
    @pytest.fixture
    def functions(self, bash):
        assert_bash_exec(
            bash,
            (
                "__tester() { "
                "local REPLY; "
                '_comp_abspath "$1"; '
                'printf %s "$REPLY"; '
                "}"
            ),
        )

    def test_non_pollution(self, bash):
        """Test environment non-pollution, detected at teardown."""
        assert_bash_exec(
            bash,
            "foo() { local REPLY=; _comp_abspath bar; }; foo; unset -f foo",
            want_output=None,
        )

    def test_absolute(self, bash, functions):
        output = assert_bash_exec(
            bash,
            "__tester /foo/bar",
            want_output=True,
            want_newline=False,
        )
        assert output.strip() == "/foo/bar"

    def test_relative(self, bash, functions):
        output = assert_bash_exec(
            bash,
            "__tester foo/bar",
            want_output=True,
            want_newline=False,
        )
        assert output.strip().endswith("/shared/foo/bar")

    def test_cwd(self, bash, functions):
        output = assert_bash_exec(
            bash,
            "__tester ./foo/./bar",
            want_output=True,
            want_newline=False,
        )
        assert output.strip().endswith("/shared/foo/bar")

    def test_parent(self, bash, functions):
        output = assert_bash_exec(
            bash,
            "__tester ../shared/foo/bar",
            want_output=True,
            want_newline=False,
        )
        assert output.strip().endswith(
            "/shared/foo/bar"
        ) and not output.strip().endswith("../shared/foo/bar")
