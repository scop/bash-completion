import pytest


class TestService:
    @pytest.mark.complete("service ")
    def test_1(self, completion):
        assert completion
