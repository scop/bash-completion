import pytest


class TestRlog:
    @pytest.mark.complete("rlog ")
    def test_1(self, completion):
        assert completion
