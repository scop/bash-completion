import pytest


class TestSeq:
    @pytest.mark.complete("seq --", require_longopt=True)
    def test_1(self, completion):
        assert completion
