import pytest


class TestStrip:
    @pytest.mark.complete("strip --", require_cmd=True)
    def test_1(self, completion):
        assert completion
