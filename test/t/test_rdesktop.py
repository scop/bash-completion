import pytest


class TestRdesktop:
    @pytest.mark.complete("rdesktop -")
    def test_1(self, completion):
        assert completion
