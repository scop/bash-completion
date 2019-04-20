import pytest


class TestAptitude:
    @pytest.mark.complete("aptitude ")
    def test_1(self, completion):
        assert completion
