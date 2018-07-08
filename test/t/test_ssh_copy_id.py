import pytest


@pytest.mark.bashcomp(
    pre_cmds=(
        # Some old versions of ssh-copy-id won't output even usage if no
        # identities are found. Try to make sure there is at least one.
        "HOME=$PWD/ssh-copy-id",
    ),
)
class TestSshCopyId(object):

    @pytest.mark.complete("ssh-copy-id -")
    def test_1(self, completion):
        assert completion.list
