import pytest


@pytest.mark.bashcomp(
    cmd="fprintd-delete",
)
class TestFprintdDelete:
    @pytest.mark.complete("fprintd-delete ")
    def test_basic(self, completion):
        assert completion
