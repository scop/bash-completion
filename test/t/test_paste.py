import pytest


class TestPaste:
    @pytest.mark.complete("paste ")
    def test_1(self, completion):
        assert completion
