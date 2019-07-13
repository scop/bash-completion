import pytest


class TestSort:
    @pytest.mark.complete("sort --", require_longopt=True)
    def test_1(self, completion):
        assert completion
