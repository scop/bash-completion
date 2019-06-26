import pytest


class TestSshow:
    @pytest.mark.complete("sshow -", require_cmd=True)
    def test_1(self, completion):
        assert completion
