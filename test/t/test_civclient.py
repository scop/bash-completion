import pytest


class TestCivclient:
    @pytest.mark.complete("civclient -", require_cmd=True)
    def test_1(self, completion):
        assert completion
