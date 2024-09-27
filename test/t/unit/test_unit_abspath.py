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

    def test_cwd1(self, bash, functions):
        output = assert_bash_exec(
            bash,
            "__tester ./foo/./bar",
            want_output=True,
            want_newline=False,
        )
        assert output.strip().endswith("/shared/foo/bar")

    def test_cwd2(self, bash, functions):
        output = assert_bash_exec(
            bash,
            "__tester /.",
            want_output=True,
            want_newline=False,
        )
        assert output.strip() == "/"

    def test_cwd3(self, bash, functions):
        output = assert_bash_exec(
            bash,
            "__tester /foo/.",
            want_output=True,
            want_newline=False,
        )
        assert output.strip() == "/foo"

    def test_cwd4(self, bash, functions):
        output = assert_bash_exec(
            bash,
            "__tester /././.",
            want_output=True,
            want_newline=False,
        )
        assert output.strip() == "/"

    def test_parent1(self, bash, functions):
        output = assert_bash_exec(
            bash,
            "__tester ../shared/foo/bar",
            want_output=True,
            want_newline=False,
        )
        assert output.strip().endswith(
            "/shared/foo/bar"
        ) and not output.strip().endswith("../shared/foo/bar")

    def test_parent2(self, bash, functions):
        output = assert_bash_exec(
            bash,
            "__tester /foo/..",
            want_output=True,
            want_newline=False,
        )
        assert output.strip() == "/"

    def test_parent3(self, bash, functions):
        output = assert_bash_exec(
            bash,
            "__tester /..",
            want_output=True,
            want_newline=False,
        )
        assert output.strip() == "/"

    def test_parent4(self, bash, functions):
        output = assert_bash_exec(
            bash,
            "__tester /../foo/bar",
            want_output=True,
            want_newline=False,
        )
        assert output.strip() == "/foo/bar"

    def test_parent5(self, bash, functions):
        output = assert_bash_exec(
            bash,
            "__tester /../../foo/bar",
            want_output=True,
            want_newline=False,
        )
        assert output.strip() == "/foo/bar"

    def test_parent6(self, bash, functions):
        output = assert_bash_exec(
            bash,
            "__tester /foo/../bar",
            want_output=True,
            want_newline=False,
        )
        assert output.strip() == "/bar"

    def test_parent7(self, bash, functions):
        output = assert_bash_exec(
            bash,
            "__tester /foo/../../bar",
            want_output=True,
            want_newline=False,
        )
        assert output.strip() == "/bar"

    def test_parent8(self, bash, functions):
        output = assert_bash_exec(
            bash,
            "__tester /dir1/dir2/dir3/../dir4/../../foo",
            want_output=True,
            want_newline=False,
        )
        assert output.strip() == "/dir1/foo"

    def test_parent9(self, bash, functions):
        output = assert_bash_exec(
            bash,
            "__tester //dir1/dir2///../foo",
            want_output=True,
            want_newline=False,
        )
        assert output.strip() == "/dir1/foo"

    def test_parent10(self, bash, functions):
        output = assert_bash_exec(
            bash,
            "__tester /dir1/dir2/dir3/..",
            want_output=True,
            want_newline=False,
        )
        assert output.strip() == "/dir1/dir2"

    def test_parent11(self, bash, functions):
        output = assert_bash_exec(
            bash,
            "__tester /dir1/dir2/dir3/../..",
            want_output=True,
            want_newline=False,
        )
        assert output.strip() == "/dir1"

    def test_parent12(self, bash, functions):
        output = assert_bash_exec(
            bash,
            "__tester /dir1/dir2/dir3/../../../..",
            want_output=True,
            want_newline=False,
        )
        assert output.strip() == "/"
