import pytest


@pytest.mark.bashcomp(cmd="ssh-keygen")
class TestSshKeygen:
    @pytest.mark.complete("ssh-keygen -", require_cmd=True)
    def test_1(self, completion):
        assert completion
