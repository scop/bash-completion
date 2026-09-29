import pytest


class TestUnexpand:
    @pytest.mark.complete("unexpand --", require_longopt=True)
    def test_1(self, completion):
        assert completion
