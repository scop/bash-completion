import pytest


class TestAutoheader(object):

    @pytest.mark.complete("autoheader ")
    def test_1(self, completion):
        assert completion.list
