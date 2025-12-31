import sys

import pytest

from conftest import assert_bash_exec, assert_complete, prepare_fixture_dir


@pytest.mark.bashcomp(ignore_env=r"^[+-]_comp_cmd_scp__path_esc=")
class TestSshfs:
    @pytest.mark.complete("sshfs ./")
    def test_1(self, completion):
        assert completion

    @pytest.fixture
    def tmpdir_backslash(self, bash, tmp_path_factory):
        if sys.platform.startswith("win"):
            pytest.skip("Filenames not allowed on Windows")

        tmpdir = prepare_fixture_dir(
            tmp_path_factory,
            files=["local_path-file\\"],
            dirs=["local_path-dir"],
        )
        return tmpdir

    def test_local_path_suffix_1(self, bash, tmpdir_backslash):
        completion = assert_complete(
            bash, "sshfs local_path", cwd=tmpdir_backslash
        )

        assert completion == "-dir/"

    def test_remote_path_ending_with_backslash(self, bash):
        assert_bash_exec(bash, "ssh() { echo 'hypothetical\\'; }")
        completion = assert_complete(bash, "sshfs remote_host:hypo")
        assert_bash_exec(bash, "unset -f ssh")
        assert not completion
