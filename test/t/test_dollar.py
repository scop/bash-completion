import pytest
from conftest import assert_bash_exec, assert_complete

@pytest.mark.bashcomp(cmd=None, temp_cwd=True)
class TestDollarAndBackticks:

    # ---------------------------------------------------------
    # 1. Test for boo#905348
    # ---------------------------------------------------------
    COMMANDS_905348 = ["cat", "ls", "cd"]

    @pytest.mark.parametrize("cmd", COMMANDS_905348)
    def test_variable_expansion_no_backslash_boo905348(self, bash, cmd):
        """Test that paths with variables do not get backslash-escaped (boo#905348)."""
        assert_bash_exec(bash, "mkdir -p test_dir_boo905348/logs/default_dir")

        old_delay = bash.delaybeforesend
        bash.delaybeforesend = 0.05

        completion = assert_complete(
            bash,
            f"{cmd} $FOO/logs/def",
            env={"FOO": "test_dir_boo905348"}
        )
        assert "ault_dir/" in completion
        bash.delaybeforesend = old_delay

    # ---------------------------------------------------------
    # 2. Test for boo#940835 (Command Completion with Backticks)
    # ---------------------------------------------------------
    def test_backtick_command_completion_boo940835(self, bash):
        """Test command completion after backtick without syntax error (boo#940835)."""
        completion = assert_complete(bash, "ls `fin")
        assert "`find" in completion

    # ---------------------------------------------------------
    # 3. Test for boo#963140 (Completion IN Backticks in loops)
    # ---------------------------------------------------------
    def test_completion_inside_backticks_bsc963140(self, bash):
        """Test file completion inside backticks for loops (bsc#963140)."""
        assert_bash_exec(bash, "mkdir -p test_dir_bsc963140")
        completion = assert_complete(bash, "for i in `cat test_dir_bsc")
        assert "963140/" in completion

    # ---------------------------------------------------------
    # 4. Test for boo#940837 (Variables in longopt-Commands)
    # ---------------------------------------------------------
    def test_variable_expansion_longopt_boo940837(self, bash):
        """Test variable expansion for commands using _comp_complete_longopt like ls (boo#940837)."""
        from conftest import PS1

        assert_bash_exec(bash, "mkdir -p /tmp/test_dir_boo940837")
        assert_bash_exec(bash, "export SCRATCH_AREA=/tmp/test_dir_boo940837")

        old_delay = bash.delaybeforesend
        bash.delaybeforesend = 0.05

        try:
            bash.send("ls $SCRATCH_AR\t")
            bash.expect(r"boo940837")

        finally:
            bash.sendintr()
            bash.expect_exact(PS1)

            assert_bash_exec(bash, "unset SCRATCH_AREA")
            bash.delaybeforesend = old_delay
