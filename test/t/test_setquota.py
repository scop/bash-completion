import pytest


class TestSetquota:
    @pytest.mark.complete("setquota ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("setquota -", require_cmd=True)
    def test_2(self, completion):
        assert completion
