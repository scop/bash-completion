import pytest


class TestDhclient:
    @pytest.mark.complete("dhclient -")
    def test_1(self, completion):
        assert completion
