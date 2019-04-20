import pytest


class TestSlackpkg:
    @pytest.mark.complete("slackpkg -")
    def test_1(self, completion):
        assert completion
