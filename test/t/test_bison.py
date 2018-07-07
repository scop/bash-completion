import pytest


class TestBison(object):

    @pytest.mark.complete("bison --")
    def test_1(self, completion):
        assert completion.list
