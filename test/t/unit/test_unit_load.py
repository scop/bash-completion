import os

import pytest

from conftest import assert_bash_exec, bash_env_saved, prepare_fixture_dir


@pytest.mark.bashcomp(cmd=None, cwd="_comp_load")
class TestCompLoad:
    @pytest.fixture
    def fixture_dir(self, request, bash):
        """Construct the fixture directory in a temporary directory.

        Some of the tests use specific setups of symbolic links.  However, if
        we put the symbolic links in the static fixture directory, Automake
        resolves them for tarballs.  As a result, the tests fail when the files
        are extracted from the tarballs.  There does not seem to be any option
        to change the behavior of Automake.

        We instead manually set up all symbolic links needed for the tests
        here.  The other normal files and directories are statically included
        in the repository as "/test/fixtures/_comp_load".  We first copy the
        statically included files and directories to a temporary directory and
        set up symbolic links.
        """

        tmpdir, _, _ = prepare_fixture_dir(request, files=[], dirs=[])
        assert_bash_exec(bash, "cp -R %s/* %s/" % (os.getcwd(), tmpdir))
        assert_bash_exec(bash, "mkdir -p %s/bin" % tmpdir)
        assert_bash_exec(
            bash, "ln -sf ../prefix1/bin/cmd1 %s/bin/cmd1" % tmpdir
        )
        assert_bash_exec(
            bash, "ln -sf ../prefix1/sbin/cmd2 %s/bin/cmd2" % tmpdir
        )
        return str(tmpdir)

    def test_userdir_1(self, bash, fixture_dir):
        with bash_env_saved(bash) as bash_env:
            bash_env.chdir(fixture_dir)
            bash_env.write_variable(
                "BASH_COMPLETION_USER_DIR",
                "$PWD/userdir1:$PWD/userdir2:$BASH_COMPLETION_USER_DIR",
                quote=False,
            )
            bash_env.write_variable(
                "PATH", "$PWD/prefix1/bin:$PWD/prefix1/sbin", quote=False
            )
            output = assert_bash_exec(
                bash, "_comp_load cmd1", want_output=True
            )
            assert output.strip() == "cmd1: sourced from userdir1"
            output = assert_bash_exec(
                bash, "_comp_load cmd2", want_output=True
            )
            assert output.strip() == "cmd2: sourced from userdir2"

    def test_PATH_1(self, bash, fixture_dir):
        with bash_env_saved(bash) as bash_env:
            bash_env.chdir(fixture_dir)
            bash_env.write_variable(
                "PATH", "$PWD/prefix1/bin:$PWD/prefix1/sbin", quote=False
            )
            output = assert_bash_exec(
                bash, "_comp_load cmd1", want_output=True
            )
            assert output.strip() == "cmd1: sourced from prefix1"
            output = assert_bash_exec(
                bash, "_comp_load cmd2", want_output=True
            )
            assert output.strip() == "cmd2: sourced from prefix1"
            output = assert_bash_exec(
                bash, "complete -p cmd2", want_output=True
            )
            assert " cmd2" in output
            output = assert_bash_exec(
                bash, 'complete -p "$PWD/prefix1/sbin/cmd2"', want_output=True
            )
            assert "/prefix1/sbin/cmd2" in output

    def test_cmd_path_1(self, bash, fixture_dir):
        with bash_env_saved(bash) as bash_env:
            bash_env.chdir(fixture_dir)
            assert_bash_exec(bash, "complete -r cmd1 || :", want_output=None)
            output = assert_bash_exec(
                bash, "_comp_load prefix1/bin/cmd1", want_output=True
            )
            assert output.strip() == "cmd1: sourced from prefix1"
            output = assert_bash_exec(
                bash, 'complete -p "$PWD/prefix1/bin/cmd1"', want_output=True
            )
            assert "/prefix1/bin/cmd1" in output
            assert_bash_exec(bash, "! complete -p cmd1", want_output=None)
            output = assert_bash_exec(
                bash, "_comp_load prefix1/sbin/cmd2", want_output=True
            )
            assert output.strip() == "cmd2: sourced from prefix1"
            output = assert_bash_exec(
                bash, "_comp_load bin/cmd1", want_output=True
            )
            assert output.strip() == "cmd1: sourced from prefix1"
            output = assert_bash_exec(
                bash, "_comp_load bin/cmd2", want_output=True
            )
            assert output.strip() == "cmd2: sourced from prefix1"

    def test_cmd_path_2(self, bash, fixture_dir):
        with bash_env_saved(bash) as bash_env:
            bash_env.chdir(fixture_dir)
            bash_env.write_variable("PATH", "$PWD/bin:$PATH", quote=False)
            output = assert_bash_exec(
                bash, "_comp_load cmd1", want_output=True
            )
            assert output.strip() == "cmd1: sourced from prefix1"
            output = assert_bash_exec(
                bash, "_comp_load cmd2", want_output=True
            )
            assert output.strip() == "cmd2: sourced from prefix1"

    def test_cmd_intree_precedence(self, bash, fixture_dir):
        """
        Test in-tree, i.e. completions/$cmd relative to the main script
        has precedence over location derived from PATH.
        """
        with bash_env_saved(bash) as bash_env:
            bash_env.chdir(fixture_dir)
            bash_env.write_variable("PATH", "$PWD/prefix1/bin", quote=False)
            # The in-tree `sh` completion should be loaded here,
            # and cause no output, unlike our `$PWD/prefix1/bin/sh` canary.
            assert_bash_exec(bash, "_comp_load sh", want_output=False)

    def test_option_like_cmd_name(self, bash):
        assert_bash_exec(bash, "! _comp_load -- --non-existent")
