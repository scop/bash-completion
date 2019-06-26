import pytest


class TestXrandr:
    @pytest.mark.complete("xrandr ", require_cmd=True)
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("xrandr --mode ")
    def test_2(self, completion):
        assert not completion

    @pytest.mark.complete("xrandr -", require_cmd=True)
    def test_3(self, completion):
        assert completion
