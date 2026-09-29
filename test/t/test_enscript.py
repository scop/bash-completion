import pytest


class TestEnscript:
    @pytest.mark.complete("enscript --", require_cmd=True)
    def test_1(self, completion):
        assert completion
