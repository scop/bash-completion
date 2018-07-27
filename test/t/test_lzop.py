import pytest


class TestLzop:

    @pytest.mark.complete("lzop ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("lzop ~")
    def test_2(self, completion):
        assert completion.list
