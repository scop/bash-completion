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
            output = assert_bash_exec(
                bash, "__load_completion cmd1", want_output=True
            )
            assert output.strip() == "cmd1: sourced"
            output = assert_bash_exec(
                bash, "__load_completion cmd2", want_output=True
            )
            assert output.strip() == "cmd2: sourced"

    def test_PATH_1(self, bash):
        with bash_env_saved(bash) as bash_env:
            bash_env.write_variable(
                "PATH", "$PWD/prefix1/bin:$PWD/prefix1/sbin", quote=False
            )
            output = assert_bash_exec(
                bash, "__load_completion cmd3", want_output=True
            )
            assert output.strip() == "cmd3: sourced"
            output = assert_bash_exec(
                bash, "__load_completion cmd4", want_output=True
            )
            assert output.strip() == "cmd4: sourced"

    def test_cmd_path_1(self, bash):
        output = assert_bash_exec(
            bash, "__load_completion prefix1/bin/cmd3", want_output=True
        )
        assert output.strip() == "cmd3: sourced"
        output = assert_bash_exec(
            bash, "__load_completion prefix1/sbin/cmd4", want_output=True
        )
        assert output.strip() == "cmd4: sourced"
        output = assert_bash_exec(
            bash, "__load_completion bin/cmd3", want_output=True
        )
        assert output.strip() == "cmd3: sourced"
        output = assert_bash_exec(
            bash, "__load_completion bin/cmd4", want_output=True
        )
        assert output.strip() == "cmd4: sourced"

    def test_cmd_path_2(self, bash):
        with bash_env_saved(bash) as bash_env:
            bash_env.write_variable("PATH", "$PWD/bin:$PATH", quote=False)
            output = assert_bash_exec(
                bash, "__load_completion cmd3", want_output=True
            )
            assert output.strip() == "cmd3: sourced"
            output = assert_bash_exec(
                bash, "__load_completion cmd4", want_output=True
            )
            assert output.strip() == "cmd4: sourced"
