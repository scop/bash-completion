import pytest


@pytest.mark.bashcomp(cmd="xdg-settings")
class TestXdgSettings:
    @pytest.mark.complete("xdg-settings ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("xdg-settings --", require_cmd=True)
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete("xdg-settings get ", require_cmd=True)
    def test_3(self, completion):
        assert completion
