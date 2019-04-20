import pytest


class TestCowsay:
    @pytest.mark.complete("cowsay ")
    def test_1(self, completion):
        assert completion
