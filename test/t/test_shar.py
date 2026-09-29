import pytest


class TestShar:
    @pytest.mark.complete("shar --", require_cmd=True)
    def test_1(self, completion):
        assert completion
