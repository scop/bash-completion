import pytest

from conftest import assert_bash_exec, bash_env_saved


@pytest.mark.bashcomp(cmd=None, cwd="shared", ignore_env=r"^\+COMPREPLY=")
class TestUnitRealCommand:
    def test_non_pollution(self, bash):
        """Test environment non-pollution, detected at teardown."""
        assert_bash_exec(
            bash,
            "foo() { local cur=; _realcommand bar; }; foo; unset -f foo",
            want_output=None,
        )

    def test_basename(self, bash):
        with bash_env_saved(bash) as bash_env:
            bash_env.write_variable("PATH", "$PWD/bin:$PATH", quote=False)
            output = assert_bash_exec(
                bash,
                "_realcommand arp",
                want_output=True,
            )
            assert output.strip().endswith("/shared/bin/arp")

    def test_basename_nonexistent(self, bash):
        filename = "non-existent-file-for-bash-completion-tests"
        skipif = "! type -P %s" % filename
        try:
            assert_bash_exec(bash, skipif, want_output=None)
        except AssertionError:
            pytest.skipif(skipif)
        output = assert_bash_exec(
            bash,
            "! _realcommand %s" % filename,
            want_output=False,
        )
        assert output.strip() == ""

    def test_relative(self, bash):
        output = assert_bash_exec(
            bash,
            "_realcommand bin/arp",
            want_output=True,
        )
        assert output.strip().endswith("/shared/bin/arp")

    def test_relative_nonexistent(self, bash):
        output = assert_bash_exec(
            bash,
            "! _realcommand bin/non-existent",
            want_output=False,
        )
        assert output.strip() == ""

    def test_absolute(self, bash):
        output = assert_bash_exec(
            bash,
            '_realcommand "$PWD/bin/arp"',
            want_output=True,
        )
        assert output.strip().endswith("/shared/bin/arp")

    def test_absolute_nonexistent(self, bash):
        output = assert_bash_exec(
            bash,
            '! _realcommand "$PWD/bin/non-existent"',
            want_output=False,
        )
        assert output.strip() == ""
