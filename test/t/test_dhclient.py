import pytest


class TestDhclient:
    @pytest.mark.complete("dhclient -", require_cmd=True)
    def test_1(self, completion):
        assert completion
