import pytest


class TestFusermount:

    @pytest.mark.complete("fusermount ")
    def test_1(self, completion):
        assert completion
