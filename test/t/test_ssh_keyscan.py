import pytest


@pytest.mark.bashcomp(
    cmd="ssh-keyscan",
)
class TestSshKeyscan:
    @pytest.mark.complete("ssh-keyscan ")
    def test_basic(self, completion):
        assert completion

    @pytest.mark.complete("ssh-keyscan -", require_cmd=True)
    def test_options(self, completion):
        assert completion

    @pytest.mark.complete("ssh-keyscan -t rsa,", require_cmd=True)
    def test_type_delimited(self, completion):
        assert completion
        assert "rsa" not in completion
