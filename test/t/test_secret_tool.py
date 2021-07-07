import pytest


@pytest.mark.bashcomp(cmd="secret-tool")
class TestSecretTool:
    @pytest.mark.complete("secret-tool ", require_cmd=True)
    def test_modes(self, completion):
        assert "store" in completion

    @pytest.mark.complete("secret-tool search ")
    def test_no_complete(self, completion):
        assert completion == ["--all", "--unlock"]
