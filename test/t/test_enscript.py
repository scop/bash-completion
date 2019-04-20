import pytest


class TestEnscript:
    @pytest.mark.complete("enscript --")
    def test_1(self, completion):
        assert completion
