import pytest


class TestSnownews:
    @pytest.mark.complete("snownews --")
    def test_1(self, completion):
        assert completion
