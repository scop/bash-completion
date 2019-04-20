import pytest


class TestHddtemp:
    @pytest.mark.complete("hddtemp -")
    def test_1(self, completion):
        assert completion
