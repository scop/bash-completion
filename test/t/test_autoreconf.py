import pytest


class TestAutoreconf:
    @pytest.mark.complete("autoreconf ")
    def test_1(self, completion):
        assert completion
