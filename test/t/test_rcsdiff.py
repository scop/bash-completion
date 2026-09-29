import pytest


class TestRcsdiff:
    @pytest.mark.complete("rcsdiff ")
    def test_1(self, completion):
        assert completion
