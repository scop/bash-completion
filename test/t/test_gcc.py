import pytest


class TestGcc:
    @pytest.mark.complete("gcc ")
    def test_1(self, completion):
        assert completion
