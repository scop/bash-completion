import pytest


@pytest.mark.bashcomp(
    cmd="fprintd-verify",
)
class TestFprintdVerify:
    @pytest.mark.complete("fprintd-verify ")
    def test_basic(self, completion):
        assert completion

    @pytest.mark.complete("fprintd-verify -", require_cmd=True)
    def test_options(self, completion):
        assert completion
