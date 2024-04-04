import pytest

from conftest import assert_bash_exec, bash_env_saved


@pytest.mark.bashcomp(
    cmd=None, cwd="shared", ignore_env=r"^\+declare -f __tester$"
)
class TestUnitRealCommand:
    @pytest.fixture
    def functions(self, bash):
        assert_bash_exec(
            bash,
            (
                "__tester() { "
                "local REPLY rc; "
                '_comp_realcommand "$1"; '
                "rc=$?; "
                'printf %s "$REPLY"; '
                "return $rc; "
                "}"
            ),
        )

    def test_non_pollution(self, bash):
        """Test environment non-pollution, detected at teardown."""
        assert_bash_exec(
            bash,
            "foo() { local REPLY=; _comp_realcommand bar; }; foo; unset -f foo",
            want_output=None,
        )

    def test_basename(self, bash, functions):
        with bash_env_saved(bash) as bash_env:
            bash_env.write_variable("PATH", "$PWD/bin:$PATH", quote=False)
            output = assert_bash_exec(
                bash,
                "__tester arp",
                want_output=True,
                want_newline=False,
            )
            assert output.strip().endswith("/shared/bin/arp")

    def test_basename_nonexistent(self, bash, functions):
        filename = "non-existent-file-for-bash-completion-tests"
        skipif = "! type -P %s" % filename
        try:
            assert_bash_exec(bash, skipif, want_output=None)
        except AssertionError:
            pytest.skipif(skipif)
        output = assert_bash_exec(
            bash,
            "! __tester %s" % filename,
            want_output=False,
        )
        assert output.strip() == ""

    def test_relative(self, bash, functions):
        output = assert_bash_exec(
            bash,
            "__tester bin/arp",
            want_output=True,
            want_newline=False,
        )
        assert output.strip().endswith("/shared/bin/arp")

    def test_relative_nonexistent(self, bash, functions):
        output = assert_bash_exec(
            bash,
            "! __tester bin/non-existent",
            want_output=False,
        )
        assert output.strip() == ""

    def test_absolute(self, bash, functions):
        output = assert_bash_exec(
            bash,
            '__tester "$PWD/bin/arp"',
            want_output=True,
            want_newline=False,
        )
        assert output.strip().endswith("/shared/bin/arp")

    def test_absolute_nonexistent(self, bash, functions):
        output = assert_bash_exec(
            bash,
            '! __tester "$PWD/bin/non-existent"',
            want_output=False,
        )
        assert output.strip() == ""

    def test_option_like_cmd_name(self, bash, functions):
        output = assert_bash_exec(
            bash,
            "! __tester --non-existent",
            want_output=False,
        )
        assert output.strip() == ""
