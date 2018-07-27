import pytest


class TestAutoscan:

    @pytest.mark.complete("autoscan ")
    def test_1(self, completion):
        assert completion.list
