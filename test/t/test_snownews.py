import pytest


class TestSnownews:
    @pytest.mark.complete("snownews --", require_cmd=True)
    def test_1(self, completion):
        assert completion
