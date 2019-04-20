import pytest


class TestSetquota:
    @pytest.mark.complete("setquota ")
    def test_1(self, completion):
        assert completion
