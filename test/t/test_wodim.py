import pytest


class TestWodim:
    @pytest.mark.complete("wodim ")
    def test_1(self, completion):
        assert completion
