import pytest


class TestUpdateAlternatives(object):

    @pytest.mark.complete("update-alternatives --")
    def test_1(self, completion):
        assert completion.list
