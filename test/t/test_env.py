import pytest


class TestEnv:
    @pytest.mark.complete("env --", require_longopt=True)
    def test_1(self, completion):
        assert completion
