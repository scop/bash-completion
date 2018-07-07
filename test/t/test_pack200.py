import pytest


class TestPack200(object):

    @pytest.mark.complete("pack200 ")
    def test_1(self, completion):
        assert completion.list
