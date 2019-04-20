import pytest


class TestMontage:
    @pytest.mark.complete("montage ")
    def test_1(self, completion):
        assert completion
