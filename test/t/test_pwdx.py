import pytest


class TestPwdx:
    @pytest.mark.complete("pwdx ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("pwdx -")
    def test_2(self, completion):
        assert completion
