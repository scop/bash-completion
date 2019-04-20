import pytest


class TestHost:
    @pytest.mark.complete("host -")
    def test_1(self, completion):
        assert completion
