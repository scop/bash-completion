import pytest


@pytest.mark.bashcomp(
    cmd="ssh-copy-id",
    pre_cmds=(
        # Some old versions of ssh-copy-id won't output even usage if no
        # identities are found. Try to make sure there is at least one.
        "HOME=$PWD/ssh-copy-id",
    ),
    ignore_env=r"^[+-]_scp_path_esc=",
)
class TestSshCopyId:
    @pytest.mark.complete("ssh-copy-id -", require_cmd=True)
    def test_1(self, completion):
        assert completion
