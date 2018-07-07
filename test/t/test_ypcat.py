import pytest


class TestYpcat(object):

    @pytest.mark.complete("ypcat ")
    def test_1(self, completion):
        assert completion.list
