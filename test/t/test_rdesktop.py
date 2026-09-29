import pytest


class TestRdesktop:
    @pytest.mark.complete("rdesktop -", require_cmd=True)
    def test_1(self, completion):
        assert completion
