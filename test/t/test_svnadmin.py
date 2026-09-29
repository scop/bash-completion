import pytest


class TestSvnadmin:
    @pytest.mark.complete("svnadmin ")
    def test_1(self, completion):
        assert completion
