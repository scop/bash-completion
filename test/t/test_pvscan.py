import pytest


class TestPvscan:
    @pytest.mark.complete("pvscan --")
    def test_1(self, completion):
        assert completion
