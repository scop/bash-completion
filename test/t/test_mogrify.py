import pytest


class TestMogrify:
    @pytest.mark.complete("mogrify ")
    def test_1(self, completion):
        assert completion
