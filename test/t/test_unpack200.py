import pytest


class TestUnpack200:
    @pytest.mark.complete("unpack200 ")
    def test_1(self, completion):
        assert completion
