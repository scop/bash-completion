import pytest


class TestGnokii(object):

    @pytest.mark.complete("gnokii ")
    def test_1(self, completion):
        assert completion.list
