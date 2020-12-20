import pytest


class TestNeomutt:
    @pytest.mark.complete("neomutt -")
    def test_1(self, completion):
        assert completion
