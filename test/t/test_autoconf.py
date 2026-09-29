import pytest


class TestAutoconf:
    @pytest.mark.complete("autoconf ")
    def test_1(self, completion):
        assert completion
