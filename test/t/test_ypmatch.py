import pytest


class TestYpmatch(object):

    @pytest.mark.complete("ypmatch foo ")
    def test_1(self, completion):
        assert completion.list
