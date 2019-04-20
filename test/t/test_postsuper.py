import pytest


class TestPostsuper:
    @pytest.mark.complete("postsuper ")
    def test_1(self, completion):
        assert completion
