import pytest


class TestResolvconf:
    @pytest.mark.complete("resolvconf -")
    def test_1(self, completion):
        assert completion
