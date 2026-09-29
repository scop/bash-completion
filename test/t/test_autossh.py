import pytest


class TestAutossh:
    @pytest.mark.complete("autossh -", require_cmd=True)
    def test_1(self, completion):
        assert completion
