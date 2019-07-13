import pytest


class TestExpand:
    @pytest.mark.complete("expand --", require_longopt=True)
    def test_1(self, completion):
        assert completion
