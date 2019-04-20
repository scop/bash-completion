import pytest


class TestPwd:
    @pytest.mark.complete("pwd -")
    def test_1(self, completion):
        assert completion
