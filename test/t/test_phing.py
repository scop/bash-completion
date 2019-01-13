import pytest


class TestPhing:

    @pytest.mark.complete("phing -")
    def test_1(self, completion):
        assert completion
