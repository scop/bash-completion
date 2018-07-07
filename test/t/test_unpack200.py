import pytest


class TestUnpack200(object):

    @pytest.mark.complete("unpack200 ")
    def test_1(self, completion):
        assert completion.list
