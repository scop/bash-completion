import pytest


class TestShar:
    @pytest.mark.complete("shar --")
    def test_1(self, completion):
        assert completion
