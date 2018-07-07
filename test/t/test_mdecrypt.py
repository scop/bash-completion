import pytest


class TestMdecrypt(object):

    @pytest.mark.complete("mdecrypt ")
    def test_1(self, completion):
        assert completion.list
