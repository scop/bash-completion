import pytest


class TestNmcli:
    @pytest.mark.complete("nmcli ")
    def test_1(self, completion):
        assert completion
