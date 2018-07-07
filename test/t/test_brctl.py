import pytest


class TestBrctl(object):

    @pytest.mark.complete("brctl ")
    def test_1(self, completion):
        assert completion.list
