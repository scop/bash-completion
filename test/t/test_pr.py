import pytest


class TestPr(object):

    @pytest.mark.complete("pr ")
    def test_1(self, completion):
        assert completion.list
