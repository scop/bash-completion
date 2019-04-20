import pytest


class TestCksfv:
    @pytest.mark.complete("cksfv -")
    def test_1(self, completion):
        assert completion
