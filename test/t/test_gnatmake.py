import pytest


class TestGnatmake(object):

    @pytest.mark.complete("gnatmake ")
    def test_1(self, completion):
        assert completion.list
