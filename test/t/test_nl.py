import pytest


class TestNl:
    @pytest.mark.complete("nl ")
    def test_1(self, completion):
        assert completion
