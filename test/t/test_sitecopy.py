import pytest


class TestSitecopy:
    @pytest.mark.complete("sitecopy --")
    def test_1(self, completion):
        assert completion
