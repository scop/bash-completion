import pytest


class TestXm:
    @pytest.mark.complete("xm ")
    def test_1(self, completion):
        assert completion
