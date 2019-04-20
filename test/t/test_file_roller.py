import pytest


@pytest.mark.bashcomp(cmd="file-roller")
class TestFileRoller:
    @pytest.mark.complete("file-roller ")
    def test_1(self, completion):
        assert completion
