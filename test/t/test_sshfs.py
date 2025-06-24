import pytest

from conftest import assert_bash_exec, assert_complete


@pytest.mark.bashcomp(ignore_env=r"^[+-]_comp_cmd_scp__path_esc=")
class TestSshfs:
    @pytest.mark.complete("sshfs ./")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("sshfs local_path", cwd="sshfs")
    def test_local_path_suffix_1(self, completion):
        assert completion == "-dir/"

    def test_remote_path_ending_with_backslash(self, bash):
        assert_bash_exec(bash, "ssh() { echo 'hypothetical\\'; }")
        completion = assert_complete(bash, "sshfs remote_host:hypo")
        assert_bash_exec(bash, "unset -f ssh")
        assert not completion
