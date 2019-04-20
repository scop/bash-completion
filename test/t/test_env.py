import pytest


class TestEnv:
    @pytest.mark.complete("env --", skipif="! env --help &>/dev/null")
    def test_1(self, completion):
        assert completion
