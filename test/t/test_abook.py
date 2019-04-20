import pytest


class TestAbook:
    @pytest.mark.complete("abook -")
    def test_1(self, completion):
        assert completion
