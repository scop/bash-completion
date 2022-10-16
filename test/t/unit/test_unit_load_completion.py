import pytest

from conftest import assert_bash_exec, bash_env_saved


@pytest.mark.bashcomp(cmd=None, cwd="__load_completion")
class TestLoadCompletion:
    def test_userdir_1(self, bash):
        with bash_env_saved(bash) as bash_env:
            bash_env.write_variable(
                "BASH_COMPLETION_USER_DIR",
                "$PWD/userdir1:$PWD/userdir2:$BASH_COMPLETION_USER_DIR",
                quote=False,
            )
            bash_env.write_variable(
                "PATH", "$PWD/prefix1/bin:$PWD/prefix1/sbin", quote=False
            )
            output = assert_bash_exec(
                bash, "__load_completion cmd1", want_output=True
            )
            assert output.strip() == "cmd1: sourced from userdir1"
            output = assert_bash_exec(
                bash, "__load_completion cmd2", want_output=True
            )
            assert output.strip() == "cmd2: sourced from userdir2"

    def test_PATH_1(self, bash):
        with bash_env_saved(bash) as bash_env:
            bash_env.write_variable(
                "PATH", "$PWD/prefix1/bin:$PWD/prefix1/sbin", quote=False
            )
            output = assert_bash_exec(
                bash, "__load_completion cmd1", want_output=True
            )
            assert output.strip() == "cmd1: sourced from prefix1"
            output = assert_bash_exec(
                bash, "__load_completion cmd2", want_output=True
            )
            assert output.strip() == "cmd2: sourced from prefix1"

    def test_cmd_path_1(self, bash):
        output = assert_bash_exec(
            bash, "__load_completion prefix1/bin/cmd1", want_output=True
        )
        assert output.strip() == "cmd1: sourced from prefix1"
        output = assert_bash_exec(
            bash, "__load_completion prefix1/sbin/cmd2", want_output=True
        )
        assert output.strip() == "cmd2: sourced from prefix1"
        output = assert_bash_exec(
            bash, "__load_completion bin/cmd1", want_output=True
        )
        assert output.strip() == "cmd1: sourced from prefix1"
        output = assert_bash_exec(
            bash, "__load_completion bin/cmd2", want_output=True
        )
        assert output.strip() == "cmd2: sourced from prefix1"

    def test_cmd_path_2(self, bash):
        with bash_env_saved(bash) as bash_env:
            bash_env.write_variable("PATH", "$PWD/bin:$PATH", quote=False)
            output = assert_bash_exec(
                bash, "__load_completion cmd1", want_output=True
            )
            assert output.strip() == "cmd1: sourced from prefix1"
            output = assert_bash_exec(
                bash, "__load_completion cmd2", want_output=True
            )
            assert output.strip() == "cmd2: sourced from prefix1"

    def test_cmd_intree_precedence(self, bash):
        """
        Test in-tree, i.e. completions/$cmd relative to the main script
        has precedence over location derived from PATH.
        """
        with bash_env_saved(bash) as bash_env:
            bash_env.write_variable("PATH", "$PWD/prefix1/bin", quote=False)
            # The in-tree `sh` completion should be loaded here,
            # and cause no output, unlike our `$PWD/prefix1/bin/sh` canary.
            assert_bash_exec(bash, "__load_completion sh", want_output=False)
