import pytest


class TestCfagent:
    @pytest.mark.complete("cfagent -", require_cmd=True)
    def test_1(self, completion):
        assert completion
