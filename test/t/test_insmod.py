import pytest


class TestInsmod:
    @pytest.mark.complete("insmod ")
    def test_1(self, completion):
        assert completion
