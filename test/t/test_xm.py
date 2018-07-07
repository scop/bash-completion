import pytest


class TestXm(object):

    @pytest.mark.complete("xm ")
    def test_1(self, completion):
        assert completion.list
