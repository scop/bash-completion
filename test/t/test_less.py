import pytest


class TestLess:

    @pytest.mark.complete("less --")
    def test_1(self, completion):
        assert completion
