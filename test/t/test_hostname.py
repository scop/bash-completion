import pytest


class TestHostname:
    @pytest.mark.complete("hostname -")
    def test_1(self, completion):
        assert completion
