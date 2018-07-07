import pytest


class TestJshint(object):

    @pytest.mark.complete("jshint ")
    def test_1(self, completion):
        assert completion.list
