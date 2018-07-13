import pytest


@pytest.mark.bashcomp(
    cmd="ssh-add",
)
class TestSshAdd(object):

    @pytest.mark.complete("ssh-add ")
    def test_1(self, completion):
        assert completion.list
