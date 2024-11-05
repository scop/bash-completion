import pytest


@pytest.mark.bashcomp(
    cmd="fprintd-list",
)
class TestFprintdList:
    @pytest.mark.complete("fprintd-list ")
    def test_basic(self, completion):
        assert completion
