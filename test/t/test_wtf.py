import pytest


class TestWtf:
    @pytest.mark.complete("wtf A")
    def test_1(self, completion):
        assert completion
