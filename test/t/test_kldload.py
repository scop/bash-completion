import pytest


class TestKldload:
    @pytest.mark.complete("kldload ")
    def test_1(self, completion):
        assert completion
