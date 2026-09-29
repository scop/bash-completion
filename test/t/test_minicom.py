import pytest


class TestMinicom:
    @pytest.mark.complete("minicom -", require_cmd=True)
    def test_1(self, completion):
        assert completion
