import pytest


class TestAutoupdate(object):

    @pytest.mark.complete("autoupdate ")
    def test_1(self, completion):
        assert completion.list
