import pytest


class TestPwgen:
    @pytest.mark.complete("pwgen -")
    def test_1(self, completion):
        assert completion
