import pytest


class TestDropuser(object):

    @pytest.mark.complete("dropuser ")
    def test_1(self, completion):
        assert completion.list
