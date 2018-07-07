import pytest


class TestMdtool(object):

    @pytest.mark.complete("mdtool ")
    def test_1(self, completion):
        assert completion.list
