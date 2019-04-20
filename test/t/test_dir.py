import pytest


class TestDir:
    @pytest.mark.complete("dir ")
    def test_1(self, completion):
        assert completion
