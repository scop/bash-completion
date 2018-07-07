import pytest


class TestPine(object):

    @pytest.mark.complete("pine -")
    def test_1(self, completion):
        assert completion.list
