import pytest


class TestAutossh:
    @pytest.mark.complete("autossh -")
    def test_1(self, completion):
        assert completion
