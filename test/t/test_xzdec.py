import pytest


class TestXzdec:
    @pytest.mark.complete("xzdec ")
    def test_1(self, completion):
        assert completion
