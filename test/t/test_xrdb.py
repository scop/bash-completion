import pytest


class TestXrdb(object):

    @pytest.mark.complete("xrdb ")
    def test_1(self, completion):
        assert completion.list
