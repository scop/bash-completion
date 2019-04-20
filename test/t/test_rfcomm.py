import pytest


class TestRfcomm:
    @pytest.mark.complete("rfcomm ")
    def test_1(self, completion):
        assert completion
