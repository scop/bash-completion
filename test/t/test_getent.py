import pytest


class TestGetent:
    @pytest.mark.complete("getent ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("getent -")
    def test_2(self, completion):
        assert completion
