import pytest


class TestGendiff:
    @pytest.mark.complete("gendiff ")
    def test_1(self, completion):
        assert completion
