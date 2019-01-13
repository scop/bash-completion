import pytest


class TestE2freefrag:

    @pytest.mark.complete("e2freefrag ")
    def test_1(self, completion):
        assert completion
