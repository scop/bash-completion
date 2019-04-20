import pytest


class TestPr:
    @pytest.mark.complete("pr ")
    def test_1(self, completion):
        assert completion
