import pytest


class TestEject:
    @pytest.mark.complete("eject -", require_cmd=True)
    def test_1(self, completion):
        assert completion
