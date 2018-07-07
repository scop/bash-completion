import pytest


class TestChsh(object):

    @pytest.mark.complete("chsh ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("chsh -s ")
    def test_2(self, completion):
        assert completion.list
