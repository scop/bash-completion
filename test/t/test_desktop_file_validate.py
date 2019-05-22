import pytest


@pytest.mark.bashcomp(cmd="desktop-file-validate")
class TestDesktopFileValidate:
    @pytest.mark.complete("desktop-file-validate ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("desktop-file-validate -")
    def test_2(self, completion):
        assert completion
