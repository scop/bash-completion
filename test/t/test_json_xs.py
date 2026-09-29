import pytest


class TestJsonXs:
    @pytest.mark.complete("json_xs ")
    def test_1(self, completion):
        assert not completion

    @pytest.mark.complete("json_xs -")
    def test_2(self, completion):
        assert completion
