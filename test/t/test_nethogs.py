import pytest


class TestNethogs:

    @pytest.mark.complete("nethogs ")
    def test_1(self, completion):
        assert completion
