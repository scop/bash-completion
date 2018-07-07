import pytest


class TestJarsigner(object):

    @pytest.mark.complete("jarsigner ")
    def test_1(self, completion):
        assert completion.list
