import pytest


@pytest.mark.bashcomp(cmd="update-alternatives")
class TestUpdateAlternatives:
    @pytest.mark.complete("update-alternatives --", require_cmd=True)
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("update-alternatives --", require_cmd=True)
    def test_2(self, bash, completion):
        assert all(x in completion for x in ["--list", "--remove"])
