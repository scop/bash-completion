import pytest


@pytest.mark.bashcomp(cmd="update-alternatives")
class TestUpdateAlternatives:
    @pytest.mark.complete("update-alternatives --")
    def test_1(self, completion):
        assert completion
