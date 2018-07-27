import pytest


class TestEog:

    @pytest.mark.complete("eog ")
    def test_1(self, completion):
        assert completion.list
