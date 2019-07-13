import pytest


class TestTouch:
    @pytest.mark.complete("touch --", require_longopt=True)
    def test_1(self, completion):
        assert completion
