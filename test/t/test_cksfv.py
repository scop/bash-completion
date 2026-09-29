import pytest


class TestCksfv:
    @pytest.mark.complete("cksfv -", require_cmd=True)
    def test_1(self, completion):
        assert completion
