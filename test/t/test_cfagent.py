import pytest


class TestCfagent:
    @pytest.mark.complete("cfagent -")
    def test_1(self, completion):
        assert completion
