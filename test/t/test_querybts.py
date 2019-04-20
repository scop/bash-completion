import pytest


class TestQuerybts:
    @pytest.mark.complete("querybts --")
    def test_1(self, completion):
        assert completion
