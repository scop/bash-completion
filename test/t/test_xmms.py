import pytest


class TestXmms:
    @pytest.mark.complete("xmms --")
    def test_1(self, completion):
        assert completion
