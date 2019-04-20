import pytest


class TestCfrun:
    @pytest.mark.complete("cfrun -")
    def test_1(self, completion):
        assert completion
